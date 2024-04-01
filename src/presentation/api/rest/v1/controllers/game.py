"""
game.py: File, containing twich game endpoints.
"""


from dataclasses import asdict
from typing import Annotated

from fastapi import (
    APIRouter,
    Path,
    Request,
    status,
)
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from application.commands import (
    DeleteTwichGame,
    DeleteTwichGameByName,
    ParseTwichGame,
)
from application.dto import (
    ResultDTO,
    TwichGameDTO,
    TwichGamesDTO,
)
from application.interfaces.bus import (
    ICommandBus,
    IQueryBus,
)
from application.queries import (
    GetAllTwichGames,
    GetTwichGame,
    GetTwichGameByName,
)
from presentation.api.rest.v1.metadata import TwichGameMetadata
from presentation.api.rest.v1.requests import JSONAPIPostSchema
from presentation.api.rest.v1.responses import JSONAPISuccessResponseSchema
from presentation.api.rest.v1.schemas import JSONAPIObjectSchema


class TwichGameCommandController:
    def __init__(self, command_bus: ICommandBus) -> None:
        self.command_bus: ICommandBus = command_bus

        self.router: APIRouter = APIRouter(
            prefix='/twich',
            tags=['twich'],
        )

        self.router.add_api_route(
            path='/game',
            methods=['POST'],
            endpoint=self.parse_game,
            **TwichGameMetadata.parse_game,
        )

        self.router.add_api_route(
            path='/game/{id:int}',
            methods=['DELETE'],
            endpoint=self.delete_game,
            **TwichGameMetadata.delete_game,
        )

        self.router.add_api_route(
            path='/game/{name:str}',
            methods=['DELETE'],
            endpoint=self.delete_game_by_name,
            **TwichGameMetadata.delete_game_by_name,
        )

    async def parse_game(
        self,
        request: Request,
        body: JSONAPIPostSchema,
    ) -> JSONResponse:
        name: str = body.attributes['name']

        command: ParseTwichGame = ParseTwichGame(name=name)
        result: ResultDTO = await self.command_bus.dispatch(command)

        game_id: int = result.data['id']
        resource_url: str = f'{request.url_for("get_game", id=game_id)}'

        links: dict = {
            'self': resource_url,
        }

        response_object: JSONAPIObjectSchema = JSONAPIObjectSchema(
            id=result.data['id'],
            type='game',
            attributes={},
            links=links,
        )

        response_meta: dict = {
            'status': result.status,
            'description': result.description,
        }

        response: JSONAPISuccessResponseSchema = JSONAPISuccessResponseSchema(
            data=[response_object],
            meta=response_meta,
        )

        headers: dict = {
            'Location': resource_url,
        }

        return JSONResponse(
            content=jsonable_encoder(response),
            headers=headers,
            status_code=status.HTTP_201_CREATED,
        )

    async def delete_game(
        self,
        id: Annotated[int, Path(gt=0)],
    ) -> JSONResponse:
        command: DeleteTwichGame = DeleteTwichGame(id=id)
        result: ResultDTO = await self.command_bus.dispatch(command)

        response_meta: dict = {
            'status': result.status,
            'description': result.description,
        }

        response: JSONAPISuccessResponseSchema = JSONAPISuccessResponseSchema(
            data=[],
            meta=response_meta,
        )

        return JSONResponse(
            content=jsonable_encoder(response),
            status_code=status.HTTP_200_OK,
        )

    async def delete_game_by_name(
        self,
        name: Annotated[str, Path(min_length=1, max_length=128)],
    ) -> JSONResponse:
        command: DeleteTwichGameByName = DeleteTwichGameByName(name=name)
        result: ResultDTO = await self.command_bus.dispatch(command)

        response_meta: dict = {
            'status': result.status,
            'description': result.description,
        }

        response: JSONAPISuccessResponseSchema = JSONAPISuccessResponseSchema(
            data=[],
            meta=response_meta,
        )

        return JSONResponse(
            content=jsonable_encoder(response),
            status_code=status.HTTP_200_OK,
        )


class TwichGameQueryController:
    def __init__(self, query_bus: IQueryBus) -> None:
        self.query_bus: IQueryBus = query_bus

        self.router: APIRouter = APIRouter(
            prefix='/twich',
            tags=['twich'],
        )

        self.router.add_api_route(
            path='/game/{id:int}',
            methods=['GET'],
            endpoint=self.get_game,
            **TwichGameMetadata.get_game,
        )

        self.router.add_api_route(
            path='/game/{name:str}',
            methods=['GET'],
            endpoint=self.get_game_by_name,
            **TwichGameMetadata.get_game_by_name,
        )

        self.router.add_api_route(
            path='/games',
            methods=['GET'],
            endpoint=self.get_all_games,
            **TwichGameMetadata.get_all_games,
        )

    async def get_game(
        self,
        request: Request,
        id: Annotated[int, Path(gt=0)],
    ) -> JSONResponse:
        query: GetTwichGame = GetTwichGame(id=id)
        game: TwichGameDTO = await self.query_bus.dispatch(query)

        game_attribtutes: dict = asdict(game)
        game_id: int = game_attribtutes.pop('id')

        resource_url: str = f'{request.url_for("get_game", id=game_id)}'

        links: dict = {
            'self': resource_url,
        }

        response_object: JSONAPIObjectSchema = JSONAPIObjectSchema(
            id=game_id,
            type='game',
            attributes=game_attribtutes,
            links=links,
        )

        response: JSONAPISuccessResponseSchema = JSONAPISuccessResponseSchema(
            data=[response_object],
        )

        return JSONResponse(
            content=jsonable_encoder(response),
            status_code=status.HTTP_200_OK,
        )

    async def get_game_by_name(
        self,
        request: Request,
        name: Annotated[str, Path(min_length=1, max_length=128)],
    ) -> JSONResponse:
        query: GetTwichGameByName = GetTwichGameByName(name=name)
        game: TwichGameDTO = await self.query_bus.dispatch(query)

        game_attribtutes: dict = asdict(game)
        game_id: int = game_attribtutes.pop('id')

        resource_url: str = f'{request.url_for("get_game", id=game_id)}'

        links: dict = {
            'self': resource_url,
        }

        response_object: JSONAPIObjectSchema = JSONAPIObjectSchema(
            id=game_id,
            type='game',
            attributes=game_attribtutes,
            links=links,
        )

        response: JSONAPISuccessResponseSchema = JSONAPISuccessResponseSchema(
            data=[response_object],
        )

        return JSONResponse(
            content=jsonable_encoder(response),
            status_code=status.HTTP_200_OK,
        )

    async def get_all_games(
        self,
        request: Request,
    ) -> JSONResponse:
        query: GetAllTwichGames = GetAllTwichGames()
        games: TwichGamesDTO = await self.query_bus.dispatch(query)

        response_objects: list[JSONAPIObjectSchema] = []

        for game in games.data:
            game_attribtutes: dict = asdict(game)
            game_id: int = game_attribtutes.pop('id')

            resource_url: str = f'{request.url_for("get_game", id=game_id)}'

            links: dict = {
                'self': resource_url,
            }

            response_object: JSONAPIObjectSchema = JSONAPIObjectSchema(
                id=game_id,
                type='game',
                attributes=game_attribtutes,
                links=links,
            )

            response_objects.append(response_object)

        response: JSONAPISuccessResponseSchema = JSONAPISuccessResponseSchema(
            data=response_objects,
        )

        return JSONResponse(
            content=jsonable_encoder(response),
            status_code=status.HTTP_200_OK,
        )
