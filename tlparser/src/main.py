"""
main.py: File, containing fast api application.
"""


from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from starlette.middleware.cors import CORSMiddleware
from shared.config import settings
from shared.utils import Singleton
from container import Container
from metadata import ProjectMetadata
# from presentation.api.rest.v1.routes import routers as rest_v1_routers
from application.commands import (
    DeleteTwichGame,
    ParseTwichGame,
    DeleteTwichStream,
    ParseTwichStream,
    DeleteTwichUser,
    ParseTwichUser,
)
from application.queries import (
    GetAllTwichGames,
    GetTwichGameByName,
    GetAllTwichStreams,
    GetTwichStreamByUserLogin,
    GetAllTwichUsers,
    GetTwichUserByLogin,
)
from application.handlers.command import (
    DeleteTwichGameHandler,
    ParseTwichGameHandler,
    DeleteTwichStreamHandler,
    ParseTwichStreamHandler,
    DeleteTwichUserHandler,
    ParseTwichUserHandler,
)
from application.handlers.query import (
    GetAllTwichGamesHandler,
    GetTwichGameByNameHandler,
    GetAllTwichStreamsHandler,
    GetTwichStreamByUserLoginHandler,
    GetAllTwichUsersHandler,
    GetTwichUserByLoginHandler,
)
from application.interfaces.bus import ICommandBus

# from presentation.api.graphql.routes import router as graphql_router


@Singleton
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
            version='v1',
            openapi_url=f'/{settings.API_NAME}/v1/openapi.json',
            docs_url=f'/{settings.API_NAME}/v1/docs',
            redoc_url=f'/{settings.API_NAME}/v1/redoc',
            **ProjectMetadata.metadata,
        )

        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=settings.BACKEND_CORS_ORIGINS,
            allow_credentials=True,
            allow_methods=['GET', 'HEAD', 'OPTIONS', 'POST', 'PUT', 'PATCH', 'DELETE'],
            allow_headers=['Accept', 'Accept-Language', 'Content-Language', 'Content-Type'],
        )

        # self.app.include_router(graphql_router, prefix=f'/{settings.API_NAME}/graphql')

        redis = aioredis.from_url(
            f'{settings.REDIS_PROTOCOL}://{settings.REDIS_USERNAME}:{settings.REDIS_PASSWORD}'
            f'@{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_DB_NUMBER}'
        )
        FastAPICache.init(RedisBackend(redis), prefix='fastapi-cache')

    async def composite(self) -> None:
        self.container: Container = Container()
        self.container.twich_game_kafka_dispatcher()
        self.container.twich_user_kafka_dispatcher()
        self.container.twich_stream_kafka_dispatcher()

        delete_game_handler = self.container.delete_game_handler()
        parse_game_handler = await self.container.parse_game_handler()
        command_bus: ICommandBus = self.container.in_memory_command_bus()
        command_bus.register(DeleteTwichGame, delete_game_handler)
        command_bus.register(ParseTwichGame, parse_game_handler)
        controller = self.container.twich_game_v1_controller(command_bus=command_bus)

        get_game_by_name_handler = self.container.get_twich_game_by_name_handler()
        get_all_games_handler = self.container.get_all_games_handler()
        query_bus = self.container.in_memory_query_bus()
        query_bus.register(GetTwichGameByName, get_game_by_name_handler)
        query_bus.register(GetAllTwichGames, get_all_games_handler)
        read_controller = self.container.twich_game_read_v1_controller(query_bus=query_bus)

        self.app.include_router(controller.router, prefix=f'/{settings.API_NAME}/v1')
        self.app.include_router(read_controller.router, prefix=f'/{settings.API_NAME}/v1')


application: Application = Application()
app: FastAPI = application.app


@app.on_event('startup')
async def composite() -> None:
    await application.composite()
