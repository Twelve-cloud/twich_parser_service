"""
user.py: File, containing twich user routes.
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
    TwichUserCommandController,
    TwichUserQueryController,
)
from presentation.api.rest.v1.metadata import TwichUserMetadata
from presentation.api.rest.v1.requests import JSONAPIPostSchema


router: APIRouter = APIRouter(
    prefix='/twich',
    tags=['user'],
)


@router.post(
    path='/user',
    **TwichUserMetadata.parse_user,
)
@inject
async def parse_user(
    request: Request,
    body: JSONAPIPostSchema,
    controller: TwichUserCommandController = Depends(
        Provide[RootContainer.user_container.rest_v1_user_command_controller]
    ),
) -> JSONResponse:
    return await controller.parse_user(request=request, body=body)


@router.delete(
    path='/user/{id:int}',
    **TwichUserMetadata.delete_user,
)
@inject
async def delete_user(
    id: Annotated[int, Path(gt=0)],
    controller: TwichUserCommandController = Depends(
        Provide[RootContainer.user_container.rest_v1_user_command_controller]
    ),
) -> JSONResponse:
    return await controller.delete_user(id=id)


@router.delete(
    path='/user/{login:str}',
    **TwichUserMetadata.delete_user_by_login,
)
@inject
async def delete_user_by_login(
    login: Annotated[str, Path(min_length=1, max_length=128)],
    controller: TwichUserCommandController = Depends(
        Provide[RootContainer.user_container.rest_v1_user_command_controller]
    ),
) -> JSONResponse:
    return await controller.delete_user_by_login(login=login)


@router.get(
    path='/user/{id:int}',
    **TwichUserMetadata.get_user,
)
@inject
async def get_user(
    request: Request,
    id: Annotated[int, Path(gt=0)],
    controller: TwichUserQueryController = Depends(
        Provide[RootContainer.user_container.rest_v1_user_query_controller]
    ),
) -> JSONResponse:
    return await controller.get_user(request=request, id=id)


@router.get(
    path='/user/{login:str}',
    **TwichUserMetadata.get_user_by_login,
)
@inject
async def get_user_by_login(
    request: Request,
    login: Annotated[str, Path(min_length=1, max_length=128)],
    controller: TwichUserQueryController = Depends(
        Provide[RootContainer.user_container.rest_v1_user_query_controller]
    ),
) -> JSONResponse:
    return await controller.get_user_by_login(request=request, login=login)


@router.get(
    path='/users',
    **TwichUserMetadata.get_all_users,
)
@inject
async def get_all_users(
    request: Request,
    controller: TwichUserQueryController = Depends(
        Provide[RootContainer.user_container.rest_v1_user_query_controller]
    ),
) -> JSONResponse:
    return await controller.get_all_users(request=request)
