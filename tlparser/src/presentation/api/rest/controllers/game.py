"""
game.py: File, containing endpoinds for a twich game.
"""


from typing import Annotated
from fastapi import APIRouter, Path, status
from fastapi.responses import JSONResponse
from application.commands import DeleteTwichGame, ParseTwichGame
from application.queries import GetAllTwichGames, GetTwichGameByName
from application.interfaces.bus import ICommandBus
from application.interfaces.bus import IQueryBus
from presentation.api.rest.v1.metadata.game import TwichGameMetadata


# from fastapi_cache.decorator import cache


class TwichGameController:
    def __init__(self, command_bus: ICommandBus) -> None:
        self.command_bus: ICommandBus = command_bus

        self.router: APIRouter = APIRouter(
            prefix='/twich',
            tags=['twich'],
        )

        self.router.add_api_route(
            path='/game/{game_name}',
            endpoint=self.parse_game,
            methods=['POST'],
            status_code=status.HTTP_200_OK,
            **TwichGameMetadata.parse_game
        )
        self.router.add_api_route(
            path='/game/{game_name}',
            endpoint=self.delete_game_by_name,
            methods=['DELETE'],
            status_code=status.HTTP_200_OK,
            **TwichGameMetadata.delete_game_by_name,
        )

    async def parse_game(
        self,
        game_name: Annotated[str, Path(min_length=1, max_length=128)],
    ) -> JSONResponse:
        command: ParseTwichGame = ParseTwichGame(name=game_name)
        result = await self.command_bus.dispatch(command)
        return JSONResponse(content={'result': result.result})

    async def delete_game_by_name(
        self,
        game_name: Annotated[str, Path(min_length=1, max_length=128)],
    ) -> JSONResponse:
        command: DeleteTwichGame = DeleteTwichGame(name=game_name)
        result = await self.command_bus.dispatch(command)
        return JSONResponse(content={'result': result.result})


class TwichGameReadController:
    def __init__(self, query_bus: IQueryBus) -> None:
        self.query_bus = query_bus

#     @router.get(
#         path='/games',
#         status_code=status.HTTP_200_OK,
#         **TwichGameMetadata.get_all_games,
#     )
#     # @cache(expire=60)
#     async def get_all_games(self) -> JSONResponse:
#         query: GetAllTwichGames = GetAllTwichGames()
#         games = self.query_bus.dispatch(query)
#         return JSONResponse(content={'result': games.data[0].name})

#     @router.get(
#         path='/game/{game_name}',
#         status_code=status.HTTP_200_OK,
#         **TwichGameMetadata.get_game_by_name,
#     )
#     # @cache(expire=60)
#     async def get_game_by_name(
#         self,
#         game_name: Annotated[str, Path(min_length=1, max_length=128)],
#     ) -> JSONResponse:
#         query: GetTwichGameByName = GetTwichGameByName(name=game_name)
#         games = self.query_bus.dispatch(query)
#         return JSONResponse(content={'result': games.data[0].name})
