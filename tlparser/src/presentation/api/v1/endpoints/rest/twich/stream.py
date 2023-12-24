"""
stream.py: File, containing endpoinds for a twich stream.
"""


from typing import Annotated
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Path, Response, status
from fastapi.responses import JSONResponse
from fastapi_cache.decorator import cache
from application.schemas.twich.stream_schema import TwichStreamReadSchema
from container import Container
from presentation.api.v1.endpoints.metadata.twich.stream_metadata import TwichStreamMetadata
from presentation.controllers.twich.stream_controller import TwichStreamController


router: APIRouter = APIRouter(
    prefix='/twich',
    tags=['twich'],
)


@router.post(
    path='/stream/{user_login}',
    status_code=status.HTTP_200_OK,
    **TwichStreamMetadata.parse_stream,
)
@inject
async def parse_stream(
    user_login: Annotated[str, Path(min_length=1, max_length=128)],
    controller: TwichStreamController = Depends(Provide[Container.twich_stream_w_controller]),
) -> Response:
    """
    parse_stream: Produce message to kafka to parse stream.

    Args:
        user_login (str): Login of the user.

    Returns:
        Response: HTTP status code 200.
    """

    controller.parse_stream(user_login)

    return JSONResponse(content={}, status_code=status.HTTP_200_OK)


@router.get(
    path='/private/stream/{user_login}',
    status_code=status.HTTP_200_OK,
    **TwichStreamMetadata.private_parse_stream,
)
@cache(60)
@inject
async def private_parse_stream(
    user_login: Annotated[str, Path(min_length=1, max_length=128)],
    controller: TwichStreamController = Depends(Provide[Container.twich_stream_w_controller]),
) -> TwichStreamReadSchema:
    """
    private_parse_stream: Parse twich stream and return result as TwichStreamReadSchema.

    Args:
        user_login (str): Login of the user.
        controller (TwichStreamController): Twich stream controller.

    Returns:
        TwichStreamReadSchema: Response as TwichStreamReadSchema instance.
    """

    return controller.private_parse_stream(user_login)


@router.delete(
    path='/stream/{user_login}',
    status_code=status.HTTP_204_NO_CONTENT,
    **TwichStreamMetadata.delete_stream_by_user_login,
)
@inject
async def delete_stream_by_user_login(
    user_login: Annotated[str, Path(min_length=1, max_length=128)],
    controller: TwichStreamController = Depends(Provide[Container.twich_stream_w_controller]),
) -> Response:
    """
    delete_stream_by_user_login: Delete twich stream.

    Args:
        user_login (str): Login of the user.
        controller (TwichStreamController): Twich stream controller.

    Returns:
        Response: HTTP status code 204.
    """

    controller.delete_stream_by_user_login(user_login)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get(
    path='/streams',
    status_code=status.HTTP_200_OK,
    **TwichStreamMetadata.get_all_streams,
)
@cache(expire=60)
@inject
async def get_all_streams(
    controller: TwichStreamController = Depends(Provide[Container.twich_stream_r_controller]),
) -> list[TwichStreamReadSchema]:
    """
    get_all_streams: Return all streams.

    Args:
        controller (TwichStreamController): Twich stream controller.

    Returns:
        list[TwichStreamReadSchema]: List of twich streams.
    """

    return controller.get_all_streams()


@router.get(
    path='/stream/{user_login}',
    status_code=status.HTTP_200_OK,
    **TwichStreamMetadata.get_stream_by_user_login,
)
@cache(expire=60)
@inject
async def get_stream_by_user_login(
    user_login: Annotated[str, Path(min_length=1, max_length=128)],
    controller: TwichStreamController = Depends(Provide[Container.twich_stream_r_controller]),
) -> TwichStreamReadSchema:
    """
    get_stream_by_user_login: Return twich stream by user login.

    Args:
        user_login (str): Login of the user.
        controller (TwichStreamController): Twich stream controller.

    Returns:
        TwichStreamReadSchema: TwichStreamReadSchema instance.
    """

    return controller.get_stream_by_user_login(user_login)
