"""
stream.py: File, containing twich stream routes.
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
    TwichStreamCommandController,
    TwichStreamQueryController,
)
from presentation.api.rest.v1.metadata import TwichStreamMetadata
from presentation.api.rest.v1.requests import JSONAPIPostSchema


router: APIRouter = APIRouter(
    prefix='/twich',
    tags=['stream'],
)


@router.post(
    path='/stream',
    **TwichStreamMetadata.parse_stream,
)
@inject
async def parse_stream(
    request: Request,
    body: JSONAPIPostSchema,
    controller: TwichStreamCommandController = Depends(
        Provide[RootContainer.stream_container.rest_v1_stream_command_controller]
    ),
) -> JSONResponse:
    return await controller.parse_stream(request=request, body=body)


@router.delete(
    path='/stream/{id:int}',
    **TwichStreamMetadata.delete_stream,
)
@inject
async def delete_stream(
    id: Annotated[int, Path(gt=0)],
    controller: TwichStreamCommandController = Depends(
        Provide[RootContainer.stream_container.rest_v1_stream_command_controller]
    ),
) -> JSONResponse:
    return await controller.delete_stream(id=id)


@router.delete(
    path='/stream/{user_login:str}',
    **TwichStreamMetadata.delete_stream_by_user_login,
)
@inject
async def delete_stream_by_user_login(
    user_login: Annotated[str, Path(min_length=1, max_length=128)],
    controller: TwichStreamCommandController = Depends(
        Provide[RootContainer.stream_container.rest_v1_stream_command_controller]
    ),
) -> JSONResponse:
    return await controller.delete_stream_by_user_login(user_login=user_login)


@router.get(
    path='/stream/{id:int}',
    **TwichStreamMetadata.get_stream,
)
@inject
async def get_stream(
    request: Request,
    id: Annotated[int, Path(gt=0)],
    controller: TwichStreamQueryController = Depends(
        Provide[RootContainer.stream_container.rest_v1_stream_query_controller]
    ),
) -> JSONResponse:
    return await controller.get_stream(request=request, id=id)


@router.get(
    path='/stream/{user_login:str}',
    **TwichStreamMetadata.get_stream_by_user_login,
)
@inject
async def get_stream_by_user_login(
    request: Request,
    user_login: Annotated[str, Path(min_length=1, max_length=128)],
    controller: TwichStreamQueryController = Depends(
        Provide[RootContainer.stream_container.rest_v1_stream_query_controller]
    ),
) -> JSONResponse:
    return await controller.get_stream_by_user_login(request=request, user_login=user_login)


@router.get(
    path='/streams',
    **TwichStreamMetadata.get_all_streams,
)
@inject
async def get_all_streams(
    request: Request,
    controller: TwichStreamQueryController = Depends(
        Provide[RootContainer.stream_container.rest_v1_stream_query_controller]
    ),
) -> JSONResponse:
    return await controller.get_all_streams(request=request)
