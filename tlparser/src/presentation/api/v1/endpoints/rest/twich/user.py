"""
user.py: File, containing endpoinds for a twich user.
"""


from typing import Annotated
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Path, Response, status
from fastapi.responses import JSONResponse
from fastapi_cache.decorator import cache
from application.schemas.twich.user_schema import TwichUserReadSchema
from container import Container
from presentation.api.v1.endpoints.metadata.twich.user_metadata import TwichUserMetadata
from presentation.controllers.twich.user_controller import TwichUserController


router: APIRouter = APIRouter(
    prefix='/twich',
    tags=['twich'],
)


@router.post(
    path='/user/{user_login}',
    status_code=status.HTTP_200_OK,
    **TwichUserMetadata.parse_user,
)
@inject
async def parse_user(
    user_login: Annotated[str, Path(min_length=1, max_length=128)],
    controller: TwichUserController = Depends(Provide[Container.twich_user_w_controller]),
) -> Response:
    """
    parse_user: Produce message to kafka to parse user.

    Args:
        user_login (str): Login of the user.

    Returns:
        Response: HTTP status code 200.
    """

    controller.parse_user(user_login)

    return JSONResponse(content={}, status_code=status.HTTP_200_OK)


@router.get(
    path='/private/user/{user_login}',
    status_code=status.HTTP_200_OK,
    **TwichUserMetadata.private_parse_user,
)
@cache(60)
@inject
async def private_parse_user(
    user_login: Annotated[str, Path(min_length=1, max_length=128)],
    controller: TwichUserController = Depends(Provide[Container.twich_user_w_controller]),
) -> TwichUserReadSchema:
    """
    private_parse_user: Parse twich user and return result as TwichUserReadSchema.

    Args:
        user_login (str): Login of the user.
        controller (TwichUserController): Twich user controller.

    Returns:
        TwichUserReadSchema: Response as TwichUserReadSchema instance.
    """

    return controller.private_parse_user(user_login)


@router.delete(
    path='/user/{user_login}',
    status_code=status.HTTP_204_NO_CONTENT,
    **TwichUserMetadata.delete_user_by_login,
)
@inject
async def delete_user_by_login(
    user_login: Annotated[str, Path(min_length=1, max_length=128)],
    controller: TwichUserController = Depends(Provide[Container.twich_user_w_controller]),
) -> Response:
    """
    delete_user_by_login: Delete twich user.

    Args:
        user_login (str): Login of the user.
        controller (TwichUserController): Twich user controller.

    Returns:
        Response: HTTP status code 204.
    """

    controller.delete_user_by_login(user_login)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get(
    path='/users',
    status_code=status.HTTP_200_OK,
    **TwichUserMetadata.get_all_users,
)
@cache(expire=60)
@inject
async def get_all_users(
    controller: TwichUserController = Depends(Provide[Container.twich_user_r_controller]),
) -> list[TwichUserReadSchema]:
    """
    get_all_users: Return all twich users.

    Args:
        controller (TwichUserController): Twich user controller.

    Returns:
        list[TwichUserReadSchema]: List of twich users.
    """

    return controller.get_all_users()


@router.get(
    path='/user/{user_login}',
    status_code=status.HTTP_200_OK,
    **TwichUserMetadata.get_user_by_login,
)
@cache(expire=60)
@inject
async def get_user_by_login(
    user_login: Annotated[str, Path(min_length=1, max_length=128)],
    controller: TwichUserController = Depends(Provide[Container.twich_user_r_controller]),
) -> TwichUserReadSchema:
    """
    get_user_by_login: Return twich user by login.

    Args:
        user_login (str): Login of the user.
        controller (TwichUserController): Twich user controller.

    Returns:
        TwichUserReadSchema: TwichUserReadSchema instance.
    """

    return controller.get_user_by_login(user_login)
