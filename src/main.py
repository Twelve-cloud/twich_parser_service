# """
# main.py: File, containing fast api application.
# """
#
# from contextlib import asynccontextmanager
# from typing import AsyncGenerator
#
# from container import RootContainer
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from metadata import ProjectMetadata
# from presentation.api.rest.v1.routes import rest_router
# from shared.config import settings
# from shared.utils import Singleton
#
#
# @asynccontextmanager
# async def lifespan(app: FastAPI) -> AsyncGenerator:
#     application.container.game_container.game_kafka_dispatcher()
#     application.container.stream_container.stream_kafka_dispatcher()
#     application.container.user_container.user_kafka_dispatcher()
#     yield
#
#
# @Singleton
# class Application:
#     def __init__(self) -> None:
#         self.app: FastAPI = FastAPI(
#             title=settings.PROJECT_NAME,
#             version='v1',
#             openapi_url=f'/{settings.API_NAME}/v1/openapi.json',
#             docs_url=f'/{settings.API_NAME}/v1/docs',
#             redoc_url=f'/{settings.API_NAME}/v1/redoc',
#             lifespan=lifespan,
#             **ProjectMetadata.metadata,
#         )
#
#         self.app.add_middleware(
#             CORSMiddleware,
#             allow_origins=settings.BACKEND_CORS_ORIGINS,
#             allow_credentials=True,
#             allow_methods=['GET', 'HEAD', 'OPTIONS', 'POST', 'PUT', 'PATCH', 'DELETE'],
#             allow_headers=['Accept', 'Accept-Language', 'Content-Language', 'Content-Type'],
#         )
#
#         self.app.include_router(rest_router, prefix='/api')
#
#         self.container: RootContainer = RootContainer()
#
#
# application: Application = Application()
# app: FastAPI = application.app

from fastapi import FastAPI

app = FastAPI()


@app.get('/api/v1/health')
async def health() -> dict:
    return {'status': 'ok'}


import os
import re

from uvicorn import run
from uvicorn.config import LOGGING_CONFIG


def parse_config_file(file_path: str) -> dict:
    config = {}
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            # Handle environment variables
            match = re.match(r'^(\w+)\s*=\s*\$\{_(\w+)\}', line)
            if match:
                key, env_var = match.groups()
                value = os.getenv(f'_{env_var}')
                if value is None:
                    raise ValueError(f"Environment variable _{env_var} not set")
                config[key] = value
                continue

            # Handle regular key-value pairs
            if '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()

                # Convert numeric values
                if value.isdigit():
                    value = int(value)
                elif value.replace('.', '', 1).isdigit():
                    value = float(value)
                elif value.lower() in ('true', 'false'):
                    value = value.lower() == 'true'

                config[key.strip()] = value

    return config


def main():
    config_file = '/etc/parser/parser.conf'  # Change this to your config file path
    config = parse_config_file(config_file)

    # Convert SSL version to correct format
    if 'ssl_version' in config:
        config['ssl_version'] = getattr(config['ssl_version'], 'value', config['ssl_version'])

    # Set up logging config (optional)
    logging_config = LOGGING_CONFIG
    logging_config['formatters']['default']['fmt'] = '%(asctime)s - %(levelname)s - %(message)s'

    # Prepare the final Uvicorn configuration
    uvicorn_config = {
        'app': config.get('app', 'main:app'),
        'host': config.get('host', '0.0.0.0'),
        'port': config.get('port', 8000),
        'workers': config.get('workers', None),
        'loop': config.get('loop', 'auto'),
        'ssl_keyfile': config.get('ssl_keyfile', None),
        'ssl_certfile': config.get('ssl_certfile', None),
        'ssl_ca_certs': config.get('ssl_ca_certs', None),
        'ssl_cert_reqs': config.get('ssl_cert_reqs', None),
        'reload': config.get('reload', False),
        'proxy_headers': config.get('proxy_headers', False),
        'log_config': logging_config,
    }

    # Print all configuration parameters
    print("=== Uvicorn Configuration ===")
    for key, value in uvicorn_config.items():
        print(f"{key}: {value}")
    print("============================")

    # Run Uvicorn
    run(**uvicorn_config)


if __name__ == '__main__':
    main()
