"""
game.py: File, containing endpoinds for a twich game.
"""


from typing import Annotated
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Path, Response, status
from fastapi.responses import JSONResponse
from fastapi_cache.decorator import cache
from application.schemas.twich.game_schema import TwichGameSchema
from container import Container
from presentation.api.rest.v1.metadata.twich.game_metadata import TwichGameMetadata
from presentation.controllers.twich.game_controller import TwichGameController


router: APIRouter = APIRouter(
    prefix='/twich',
    tags=['twich'],
)


@router.post(
    path='/game/{game_name}',
    status_code=status.HTTP_200_OK,
    **TwichGameMetadata.parse_game,
)
@inject
async def parse_game(
    game_name: Annotated[str, Path(min_length=1, max_length=128)],
    controller: TwichGameController = Depends(Provide[Container.twich_game_w_controller]),
) -> Response:
    """
    parse_game: Produce message to kafka to parse games.

    Args:
        game_name (str): Identifier of the game.

    Returns:
        Response: HTTP status code 200.
    """

    await controller.parse_game(game_name)

    return JSONResponse(content={}, status_code=status.HTTP_200_OK)


@router.get(
    path='/private/game/{game_name}',
    status_code=status.HTTP_200_OK,
    **TwichGameMetadata.private_parse_game,
)
@cache(60)
@inject
async def private_parse_game(
    game_name: Annotated[str, Path(min_length=1, max_length=128)],
    controller: TwichGameController = Depends(Provide[Container.twich_game_w_controller]),
) -> TwichGameSchema:
    """
    private_parse_game: Parse twich game and return result as TwichGameSchema.

    Args:
        game_name (str): Identifier of the game.
        controller (TwichGameController): Twich game controller.

    Returns:
        TwichGameSchema: Response as TwichGameSchema instance.
    """

    return await controller.private_parse_game(game_name)


@router.delete(
    path='/game/{game_name}',
    status_code=status.HTTP_204_NO_CONTENT,
    **TwichGameMetadata.delete_game_by_name,
)
@inject
async def delete_game_by_name(
    game_name: Annotated[str, Path(min_length=1, max_length=128)],
    controller: TwichGameController = Depends(Provide[Container.twich_game_w_controller]),
) -> Response:
    """
    delete_game_by_name: Delete twich game.

     Args:
        game_name (str): Identifier of the game.
        controller (TwichGameController): Twich game controller.

    Returns:
        Response: HTTP status code 204.
    """

    await controller.delete_game_by_name(game_name)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get(
    path='/games',
    status_code=status.HTTP_200_OK,
    **TwichGameMetadata.get_all_games,
)
@cache(expire=60)
@inject
async def get_all_games(
    controller: TwichGameController = Depends(Provide[Container.twich_game_r_controller]),
) -> list[TwichGameSchema]:
    """
    get_all_games: Return all twich games.

    Args:
        controller (TwichGameController): Twich game controller.

    Returns:
        list[TwichGameSchema]: List of twich games.
    """

    return await controller.get_all_games()


@router.get(
    path='/game/{game_name}',
    status_code=status.HTTP_200_OK,
    **TwichGameMetadata.get_game_by_name,
)
@cache(expire=60)
@inject
async def get_game_by_name(
    game_name: Annotated[str, Path(min_length=1, max_length=128)],
    controller: TwichGameController = Depends(Provide[Container.twich_game_r_controller]),
) -> TwichGameSchema:
    """
    get_game_by_name: Return game by name.

    Args:
        game_name (str): Identifier of the game.
        controller (TwichGameController): Twich game controller.

    Returns:
        TwichGameSchema: TwichGameSchema instance.
    """

    return await controller.get_game_by_name(game_name)
