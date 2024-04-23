"""
game.py: File, containing twich game routes.
"""


from typing import Annotated

from dependency_injector.wiring import (
    Provide,
    inject,
)
from fastapi import (
    APIRouter,
    Depends,
    Path,
    Request,
)
from fastapi.responses import JSONResponse

from container import RootContainer
from presentation.api.rest.v1.controllers import (
    TwichGameCommandController,
    TwichGameQueryController,
)
from presentation.api.rest.v1.metadata import TwichGameMetadata
from presentation.api.rest.v1.requests import JSONAPIPostSchema


router: APIRouter = APIRouter(
    prefix='/twich',
    tags=['game'],
)


@router.post(
    path='/game',
    **TwichGameMetadata.parse_game,
)
@inject
async def parse_game(
    request: Request,
    body: JSONAPIPostSchema,
    controller: TwichGameCommandController = Depends(
        Provide[RootContainer.game_container.rest_v1_game_command_controller]
    ),
) -> JSONResponse:
    return await controller.parse_game(request=request, body=body)


@router.delete(
    path='/game/{id:int}',
    **TwichGameMetadata.delete_game,
)
@inject
async def delete_game(
    id: Annotated[int, Path(gt=0)],
    controller: TwichGameCommandController = Depends(
        Provide[RootContainer.game_container.rest_v1_game_command_controller]
    ),
) -> JSONResponse:
    return await controller.delete_game(id=id)


@router.delete(
    path='/game/{name:str}',
    **TwichGameMetadata.delete_game_by_name,
)
@inject
async def delete_game_by_name(
    name: Annotated[str, Path(min_length=1, max_length=128)],
    controller: TwichGameCommandController = Depends(
        Provide[RootContainer.game_container.rest_v1_game_command_controller]
    ),
) -> JSONResponse:
    return await controller.delete_game_by_name(name=name)


@router.get(
    path='/game/{id:int}',
    **TwichGameMetadata.get_game,
)
@inject
async def get_game(
    request: Request,
    id: Annotated[int, Path(gt=0)],
    controller: TwichGameQueryController = Depends(
        Provide[RootContainer.game_container.rest_v1_game_query_controller]
    ),
) -> JSONResponse:
    return await controller.get_game(request=request, id=id)


@router.get(
    path='/game/{name:str}',
    **TwichGameMetadata.get_game_by_name,
)
@inject
async def get_game_by_name(
    request: Request,
    name: Annotated[str, Path(min_length=1, max_length=128)],
    controller: TwichGameQueryController = Depends(
        Provide[RootContainer.game_container.rest_v1_game_query_controller]
    ),
) -> JSONResponse:
    return await controller.get_game_by_name(request=request, name=name)


@router.get(
    path='/games',
    **TwichGameMetadata.get_all_games,
)
@inject
async def get_all_games(
    request: Request,
    controller: TwichGameQueryController = Depends(
        Provide[RootContainer.game_container.rest_v1_game_query_controller]
    ),
) -> JSONResponse:
    return await controller.get_all_games(request=request)
