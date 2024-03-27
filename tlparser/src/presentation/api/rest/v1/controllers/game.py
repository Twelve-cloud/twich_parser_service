"""
game.py: File, containing endpoinds for a twich game.
"""


from typing import Annotated
from fastapi import APIRouter, Path, status
from fastapi.responses import JSONResponse
from application.commands import DeleteTwichGame, ParseTwichGame
from application.queries import GetAllTwichGames, GetTwichGameByName
from application import dto
from application.interfaces.bus import ICommandBus
from application.interfaces.bus import IQueryBus
from presentation.api.rest.v1.metadata.game import TwichGameMetadata
from dataclasses import asdict


class TwichGameController:
    def __init__(self, command_bus: ICommandBus) -> None:
        self.command_bus: ICommandBus = command_bus

        self.router: APIRouter = APIRouter(
            prefix='/twich',
            tags=['twich'],
        )

        self.router.add_api_route(
            path='/game/{name}',
            methods=['POST'],
            endpoint=self.parse_game,
            status_code=status.HTTP_201_CREATED,
            **TwichGameMetadata.parse_game,
        )

        self.router.add_api_route(
            path='/game/{name}',
            methods=['DELETE'],
            endpoint=self.delete_game,
            status_code=status.HTTP_200_OK,
            **TwichGameMetadata.delete_game,
        )

    async def parse_game(
        self,
        name: Annotated[str, Path(min_length=1, max_length=128)],
    ) -> JSONResponse:
        command: ParseTwichGame = ParseTwichGame(name=name)
        result = await self.command_bus.dispatch(command)

        return JSONResponse(content={'result': result.data})

    async def delete_game(
        self,
        name: Annotated[str, Path(min_length=1, max_length=128)],
    ) -> JSONResponse:
        command: DeleteTwichGame = DeleteTwichGame(name=name)
        result = await self.command_bus.dispatch(command)

        return JSONResponse(content={'result': result.data})


class TwichGameReadController:
    def __init__(self, query_bus: IQueryBus) -> None:
        self.query_bus = query_bus

        self.router: APIRouter = APIRouter(
            prefix='/twich',
            tags=['twich'],
        )

        self.router.add_api_route(
            path='/game/{name}',
            methods=['GET', 'HEAD'],
            endpoint=self.get_game_by_name,
            status_code=status.HTTP_200_OK,
            **TwichGameMetadata.get_game_by_name,
        )

        self.router.add_api_route(
            path='/games',
            methods=['GET', 'HEAD'],
            endpoint=self.get_all_games,
            status_code=status.HTTP_200_OK,
            **TwichGameMetadata.get_all_games,
        )

    async def get_game_by_name(
        self,
        name: Annotated[str, Path(min_length=1, max_length=128)],
    ) -> JSONResponse:
        query: GetTwichGameByName = GetTwichGameByName(name=name)
        game: dto.TwichGameDTO = await self.query_bus.dispatch(query)

        return JSONResponse(content={'result': asdict(game)})

    async def get_all_games(self) -> JSONResponse:
        query: GetAllTwichGames = GetAllTwichGames()
        games: list[dto.TwichGameDTO] = await self.query_bus.dispatch(query)

        return JSONResponse(content={'result': [asdict(game) for game in games.data]})
