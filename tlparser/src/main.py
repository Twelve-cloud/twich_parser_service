"""
main.py: File, containing fast api application.
"""


from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from starlette.middleware.cors import CORSMiddleware
from common.config.base.settings import settings
from common.utils.decorators import singleton
from container import Container
from metadata import ProjectMetadata
from presentation.api.v1.routes import routers as rest_v1_routers


@singleton
class Application:
    """
    Application: Class, containing fast api application, application container.
    """

    def __init__(self) -> None:
        """
        __init__: Set up fast api app (routers, cors, etc..) and wire dependencies.
        """

        self.app: FastAPI = FastAPI(
            title=settings.PROJECT_NAME,
            version=settings.API_SEM_VERSION,
            openapi_url=f'/{settings.API_NAME}/{settings.API_VERSION}/openapi.json',
            docs_url=f'/{settings.API_NAME}/{settings.API_VERSION}/docs',
            redoc_url=f'/{settings.API_NAME}/{settings.API_VERSION}/redoc',
            **ProjectMetadata.metadata,
        )

        self.container: Container = Container()

        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=settings.BACKEND_CORS_ORIGINS,
            allow_credentials=True,
            allow_methods=['GET', 'HEAD', 'OPTIONS', 'POST', 'PUT', 'PATCH', 'DELETE'],
            allow_headers=['Accept', 'Accept-Language', 'Content-Language', 'Content-Type'],
        )

        self.app.include_router(rest_v1_routers, prefix=f'/{settings.API_NAME}')


application: Application = Application()
app: FastAPI = application.app


@app.on_event("startup")
async def startup() -> None:
    redis = aioredis.from_url(
        f'{settings.REDIS_PROTOCOL}://{settings.REDIS_USERNAME}:{settings.REDIS_PASSWORD}'
        f'@{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_DB_NUMBER}'
    )
    FastAPICache.init(RedisBackend(redis), prefix='fastapi-cache')
