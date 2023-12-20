"""
main.py: File, containing fast api application.
"""


from common.config.base.settings import settings
from common.utils.decorators import singleton
from container import Container
from fastapi import FastAPI
from metadata import ProjectMetadata
from presentation.api.v1.routes import routers as rest_v1_routers
from starlette.middleware.cors import CORSMiddleware


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
