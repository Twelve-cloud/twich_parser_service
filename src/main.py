"""
main.py: File, containing fast api application.
"""


from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from starlette.middleware.cors import CORSMiddleware

from container import Container
from metadata import ProjectMetadata
from shared.config import settings
from shared.utils import Singleton


# from presentation.api.rest.v1.routes import routers as rest_v1_routers

from application.commands import (
    DeleteTwichGame,
    DeleteTwichGameByName,
    DeleteTwichStream,
    DeleteTwichStreamByUserLogin,
    DeleteTwichUser,
    DeleteTwichUserByLogin,
    ParseTwichGame,
    ParseTwichStream,
    ParseTwichUser,
)
from application.interfaces.bus import (
    ICommandBus,
    IQueryBus,
)
from application.queries import (
    GetAllTwichGames,
    GetAllTwichStreams,
    GetAllTwichUsers,
    GetTwichGame,
    GetTwichGameByName,
    GetTwichStream,
    GetTwichStreamByUserLogin,
    GetTwichUser,
    GetTwichUserByLogin,
)


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

        command_bus: ICommandBus = self.container.in_memory_command_bus()
        query_bus: IQueryBus = self.container.in_memory_query_bus()

        delete_game_handler = self.container.delete_game_handler()
        delete_game_by_name_handler = self.container.delete_game_by_name_handler()
        parse_game_handler = await self.container.parse_game_handler()
        command_bus.register(DeleteTwichGame, delete_game_handler)
        command_bus.register(DeleteTwichGameByName, delete_game_by_name_handler)
        command_bus.register(ParseTwichGame, parse_game_handler)

        get_game_by_name_handler = self.container.get_twich_game_by_name_handler()
        get_game_handler = self.container.get_twich_game_handler()
        get_all_games_handler = self.container.get_all_games_handler()
        query_bus.register(GetTwichGameByName, get_game_by_name_handler)
        query_bus.register(GetTwichGame, get_game_handler)
        query_bus.register(GetAllTwichGames, get_all_games_handler)

        game_controller = self.container.twich_game_v1_controller(command_bus=command_bus)
        game_read_controller = self.container.twich_game_read_v1_controller(query_bus=query_bus)

        delete_stream_handler = self.container.delete_stream_handler()
        delete_stream_by_user_login_handler = self.container.delete_stream_by_user_login_handler()
        parse_stream_handler = await self.container.parse_stream_handler()
        command_bus.register(DeleteTwichStream, delete_stream_handler)
        command_bus.register(DeleteTwichStreamByUserLogin, delete_stream_by_user_login_handler)
        command_bus.register(ParseTwichStream, parse_stream_handler)

        get_stream_by_user_login_handler = self.container.get_twich_stream_by_user_login_handler()
        get_stream_handler = self.container.get_twich_stream_handler()
        get_all_streams_handler = self.container.get_all_streams_handler()
        query_bus.register(GetTwichStreamByUserLogin, get_stream_by_user_login_handler)
        query_bus.register(GetTwichStream, get_stream_handler)
        query_bus.register(GetAllTwichStreams, get_all_streams_handler)

        stream_controller = self.container.twich_stream_v1_controller(command_bus=command_bus)
        stream_read_controller = self.container.twich_stream_read_v1_controller(query_bus=query_bus)

        delete_user_handler = self.container.delete_user_handler()
        delete_user_by_login_handler = self.container.delete_user_by_login_handler()
        parse_user_handler = await self.container.parse_user_handler()
        command_bus.register(DeleteTwichUser, delete_user_handler)
        command_bus.register(DeleteTwichUserByLogin, delete_user_by_login_handler)
        command_bus.register(ParseTwichUser, parse_user_handler)

        get_user_by_login_handler = self.container.get_twich_user_by_login_handler()
        get_user_handler = self.container.get_twich_user_handler()
        get_all_users_handler = self.container.get_all_users_handler()
        query_bus.register(GetTwichUserByLogin, get_user_by_login_handler)
        query_bus.register(GetTwichUser, get_user_handler)
        query_bus.register(GetAllTwichUsers, get_all_users_handler)

        user_controller = self.container.twich_user_v1_controller(command_bus=command_bus)
        user_read_controller = self.container.twich_user_read_v1_controller(query_bus=query_bus)

        self.app.include_router(game_controller.router, prefix=f'/{settings.API_NAME}/v1')
        self.app.include_router(game_read_controller.router, prefix=f'/{settings.API_NAME}/v1')
        self.app.include_router(stream_controller.router, prefix=f'/{settings.API_NAME}/v1')
        self.app.include_router(stream_read_controller.router, prefix=f'/{settings.API_NAME}/v1')
        self.app.include_router(user_controller.router, prefix=f'/{settings.API_NAME}/v1')
        self.app.include_router(user_read_controller.router, prefix=f'/{settings.API_NAME}/v1')


application: Application = Application()
app: FastAPI = application.app


@app.on_event('startup')
async def composite() -> None:
    await application.composite()
