"""
stream.py: File, containing twich stream endpoints.
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
    DeleteTwichStream,
    DeleteTwichStreamByUserLogin,
    ParseTwichStream,
)
from application.dto import (
    ResultDTO,
    TwichStreamDTO,
    TwichStreamsDTO,
)
from application.interfaces.bus import (
    ICommandBus,
    IQueryBus,
)
from application.queries import (
    GetAllTwichStreams,
    GetTwichStream,
    GetTwichStreamByUserLogin,
)
from presentation.api.rest.v1.metadata import TwichStreamMetadata
from presentation.api.rest.v1.requests import JSONAPIPostSchema
from presentation.api.rest.v1.responses import JSONAPISuccessResponseSchema
from presentation.api.rest.v1.schemas import JSONAPIObjectSchema


class TwichStreamCommandController:
    def __init__(self, command_bus: ICommandBus) -> None:
        self.command_bus: ICommandBus = command_bus

        self.router: APIRouter = APIRouter(
            prefix='/twich',
            tags=['twich'],
        )

        self.router.add_api_route(
            path='/stream',
            methods=['POST'],
            endpoint=self.parse_stream,
            **TwichStreamMetadata.parse_stream,
        )

        self.router.add_api_route(
            path='/stream/{id:int}',
            methods=['DELETE'],
            endpoint=self.delete_stream,
            **TwichStreamMetadata.delete_stream,
        )

        self.router.add_api_route(
            path='/stream/{user_login:str}',
            methods=['DELETE'],
            endpoint=self.delete_stream_by_user_login,
            **TwichStreamMetadata.delete_stream_by_user_login,
        )

    async def parse_stream(
        self,
        request: Request,
        body: JSONAPIPostSchema,
    ) -> JSONResponse:
        user_login: str = body.attributes['user_login']

        command: ParseTwichStream = ParseTwichStream(user_login=user_login)
        result: ResultDTO = await self.command_bus.dispatch(command)

        stream_id: int = result.data['id']
        resource_url: str = f'{request.url_for("get_stream", id=stream_id)}'

        links: dict = {
            'self': resource_url,
        }

        response_object: JSONAPIObjectSchema = JSONAPIObjectSchema(
            id=result.data['id'],
            type='stream',
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

    async def delete_stream(
        self,
        id: Annotated[int, Path(gt=0)],
    ) -> JSONResponse:
        command: DeleteTwichStream = DeleteTwichStream(id=id)
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

    async def delete_stream_by_user_login(
        self,
        user_login: Annotated[str, Path(min_length=1, max_length=128)],
    ) -> JSONResponse:
        command: DeleteTwichStreamByUserLogin = DeleteTwichStreamByUserLogin(user_login=user_login)
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


class TwichStreamQueryController:
    def __init__(self, query_bus: IQueryBus) -> None:
        self.query_bus: IQueryBus = query_bus

        self.router: APIRouter = APIRouter(
            prefix='/twich',
            tags=['twich'],
        )

        self.router.add_api_route(
            path='/stream/{id:int}',
            methods=['GET'],
            endpoint=self.get_stream,
            **TwichStreamMetadata.get_stream,
        )

        self.router.add_api_route(
            path='/stream/{user_login:str}',
            methods=['GET'],
            endpoint=self.get_stream_by_user_login,
            **TwichStreamMetadata.get_stream_by_user_login,
        )

        self.router.add_api_route(
            path='/streams',
            methods=['GET'],
            endpoint=self.get_all_streams,
            **TwichStreamMetadata.get_all_streams,
        )

    async def get_stream(
        self,
        request: Request,
        id: Annotated[int, Path(gt=0)],
    ) -> JSONResponse:
        query: GetTwichStream = GetTwichStream(id=id)
        stream: TwichStreamDTO = await self.query_bus.dispatch(query)

        stream_attribtutes: dict = asdict(stream)
        stream_id: int = stream_attribtutes.pop('id')

        resource_url: str = f'{request.url_for("get_stream", id=stream_id)}'

        links: dict = {
            'self': resource_url,
        }

        response_object: JSONAPIObjectSchema = JSONAPIObjectSchema(
            id=stream_id,
            type='stream',
            attributes=stream_attribtutes,
            links=links,
        )

        response: JSONAPISuccessResponseSchema = JSONAPISuccessResponseSchema(
            data=[response_object],
        )

        return JSONResponse(
            content=jsonable_encoder(response),
            status_code=status.HTTP_200_OK,
        )

    async def get_stream_by_user_login(
        self,
        request: Request,
        user_login: Annotated[str, Path(min_length=1, max_length=128)],
    ) -> JSONResponse:
        query: GetTwichStreamByUserLogin = GetTwichStreamByUserLogin(user_login=user_login)
        stream: TwichStreamDTO = await self.query_bus.dispatch(query)

        stream_attribtutes: dict = asdict(stream)
        stream_id: int = stream_attribtutes.pop('id')

        resource_url: str = f'{request.url_for("get_stream", id=stream_id)}'

        links: dict = {
            'self': resource_url,
        }

        response_object: JSONAPIObjectSchema = JSONAPIObjectSchema(
            id=stream_id,
            type='stream',
            attributes=stream_attribtutes,
            links=links,
        )

        response: JSONAPISuccessResponseSchema = JSONAPISuccessResponseSchema(
            data=[response_object],
        )

        return JSONResponse(
            content=jsonable_encoder(response),
            status_code=status.HTTP_200_OK,
        )

    async def get_all_streams(
        self,
        request: Request,
    ) -> JSONResponse:
        query: GetAllTwichStreams = GetAllTwichStreams()
        streams: TwichStreamsDTO = await self.query_bus.dispatch(query)

        response_objects: list[JSONAPIObjectSchema] = []

        for stream in streams.data:
            stream_attribtutes: dict = asdict(stream)
            stream_id: int = stream_attribtutes.pop('id')

            resource_url: str = f'{request.url_for("get_stream", id=stream_id)}'

            links: dict = {
                'self': resource_url,
            }

            response_object: JSONAPIObjectSchema = JSONAPIObjectSchema(
                id=stream_id,
                type='stream',
                attributes=stream_attribtutes,
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
