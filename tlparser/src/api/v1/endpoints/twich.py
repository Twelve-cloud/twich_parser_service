"""
twich.py: File, containing endpoinds for a twich app.
"""


from fastapi import Depends, APIRouter, status
from config.metadata import parse_game_metadata, parse_user_metadata, parse_stream_metadata
from core.containers import Container
from schemas.twich_schemas import TwichGameSchema, TwichUserSchema, TwichStreamSchema
from dependency_injector.wiring import Provide, inject
from controllers.twich_controllers import TwichController


router: APIRouter = APIRouter(
    prefix='/twich',
    tags=['twich'],
)


@router.post('/parse/game/{game_id}', status_code=status.HTTP_200_OK, **parse_game_metadata)
@inject
async def parse_game(
    game_id: str, controller: TwichController = Depends(Provide[Container.twich_controller])
) -> TwichGameSchema:
    """
    parse_game: Parse twich game and return result as TwichGameSchema.

    Args:
        game_id (str): Identifier of the game.
        controller (TwichController): Twich controller.

    Returns:
        TwichGameSchema: Response as TwichGameSchema instance.
    """

    return await controller.parse_game(game_id)


@router.post('/parse/user/{user_id}', status_code=status.HTTP_200_OK, **parse_user_metadata)
@inject
async def parse_user(
    user_id: str, controller: TwichController = Depends(Provide[Container.twich_controller])
) -> TwichUserSchema:
    """
    parse_user: Parse twich user and return result as TwichUserSchema.

    Args:
        user_id (str): Identifier of the user.
        controller (TwichController): Twich controller.

    Returns:
        TwichUserSchema: Response as TwichUserSchema instance.
    """

    return await controller.parse_user(user_id)


@router.post('/parse/stream/{user_id}', status_code=status.HTTP_200_OK, **parse_stream_metadata)
@inject
async def parse_stream(
    user_id: str, controller: TwichController = Depends(Provide[Container.twich_controller])
) -> TwichStreamSchema:
    """
    parse_stream: Parse twich stream and return result as TwichStreamSchema.

    Args:
        user_id (str): Identifier of the user.
        game_id (str): Identifier of the game.
        controller (TwichController): Twich controller.

    Returns:
        TwichStreamSchema: Response as TwichStreamSchema instance.
    """

    return await controller.parse_stream(user_id)
