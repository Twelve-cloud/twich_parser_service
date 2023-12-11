"""
main.py: File, containing fast api application.
"""


from fastapi import FastAPI
from api.v1.routes import routers as rest_v1_routers
from config.metadata import project_metadata
from config.settings import settings
from core.containers import Container
from core.decorators import singleton
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
            **project_metadata,
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
