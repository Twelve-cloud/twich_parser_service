"""
game.py: File, containing endpoinds for a twich game.
"""


from typing import Annotated
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Path, status
from application.dtos.requests.game import (
    DeleteTwichGameByNameRequest,
    GetTwichGameByNameRequest,
    ParseTwichGameRequest,
)
from application.dtos.responses.game import (
    DeleteTwichGameByNameResponse,
    GetTwichGameByNameResponse,
    ParseTwichGameResponse,
)
from application.services.decorators import ServiceDecorator
from container import Container
from presentation.api.rest.v1.metadata.game import TwichGameMetadata


# from fastapi_cache.decorator import cache


router: APIRouter = APIRouter(
    prefix='/twich',
    tags=['twich'],
)


@router.get(
    path='/private/game/{game_name}',
    status_code=status.HTTP_200_OK,
    **TwichGameMetadata.private_parse_game,
)
# @cache(60)
@inject
async def private_parse_game(
    game_name: Annotated[str, Path(min_length=1, max_length=128)],
    service_decorator: ServiceDecorator = Depends(
        Provide[Container.twich_game_w_service_decorator]
    ),
) -> ParseTwichGameResponse:
    """
    private_parse_game: Parse twich game and return result as TwichGameSchema.

    Args:
        game_name (str): Identifier of the game.
        service_decorator (ServiceDecorator): Twich game service_decorator.

    Returns:
        TwichGameSchema: Response as TwichGameSchema instance.
    """

    request: ParseTwichGameRequest = ParseTwichGameRequest(name=game_name)
    return await service_decorator.private_parse_game(request)


@router.delete(
    path='/game/{game_name}',
    status_code=status.HTTP_200_OK,
    **TwichGameMetadata.delete_game_by_name,
)
@inject
async def delete_game_by_name(
    game_name: Annotated[str, Path(min_length=1, max_length=128)],
    service_decorator: ServiceDecorator = Depends(
        Provide[Container.twich_game_w_service_decorator]
    ),
) -> DeleteTwichGameByNameResponse:
    """
    delete_game_by_name: Delete twich game.

     Args:
        game_name (str): Identifier of the game.
        service_decorator (ServiceDecorator): Twich game service_decorator.

    Returns:
        Response: HTTP status code 204.
    """

    request: DeleteTwichGameByNameRequest = DeleteTwichGameByNameRequest(name=game_name)
    return await service_decorator.delete_game_by_name(request)


@router.get(
    path='/games',
    status_code=status.HTTP_200_OK,
    **TwichGameMetadata.get_all_games,
)
# @cache(expire=60)
@inject
async def get_all_games(
    service_decorator: ServiceDecorator = Depends(
        Provide[Container.twich_game_r_service_decorator]
    ),
) -> list[GetTwichGameByNameResponse]:
    """
    get_all_games: Return all twich games.

    Args:
        service_decorator (ServiceDecorator): Twich game service_decorator.

    Returns:
        list[TwichGameSchema]: List of twich games.
    """

    return await service_decorator.get_all_games()


@router.get(
    path='/game/{game_name}',
    status_code=status.HTTP_200_OK,
    **TwichGameMetadata.get_game_by_name,
)
# @cache(expire=60)
@inject
async def get_game_by_name(
    game_name: Annotated[str, Path(min_length=1, max_length=128)],
    service_decorator: ServiceDecorator = Depends(
        Provide[Container.twich_game_r_service_decorator]
    ),
) -> GetTwichGameByNameResponse:
    """
    get_game_by_name: Return game by name.

    Args:
        game_name (str): Identifier of the game.
        service_decorator (ServiceDecorator): Twich game service_decorator.

    Returns:
        TwichGameSchema: TwichGameSchema instance.
    """

    request: GetTwichGameByNameRequest = GetTwichGameByNameRequest(name=game_name)
    return await service_decorator.get_game_by_name(request)
