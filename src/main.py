"""
main.py: File, containing fast api application.
"""


from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from container import RootContainer
from metadata import ProjectMetadata
from presentation.api.rest.v1.routes import rest_router
from shared.config import settings
from shared.utils import Singleton


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    application.container.game_container.game_kafka_dispatcher()
    application.container.stream_container.stream_kafka_dispatcher()
    application.container.user_container.user_kafka_dispatcher()
    yield


@Singleton
class Application:
    def __init__(self) -> None:
        self.app: FastAPI = FastAPI(
            title=settings.PROJECT_NAME,
            version='v1',
            openapi_url=f'/{settings.API_NAME}/v1/openapi.json',
            docs_url=f'/{settings.API_NAME}/v1/docs',
            redoc_url=f'/{settings.API_NAME}/v1/redoc',
            lifespan=lifespan,
            **ProjectMetadata.metadata,
        )

        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=settings.BACKEND_CORS_ORIGINS,
            allow_credentials=True,
            allow_methods=['GET', 'HEAD', 'OPTIONS', 'POST', 'PUT', 'PATCH', 'DELETE'],
            allow_headers=['Accept', 'Accept-Language', 'Content-Language', 'Content-Type'],
        )

        self.app.include_router(rest_router, prefix='/api')

        self.container = RootContainer()


application: Application = Application()
app: FastAPI = application.app
