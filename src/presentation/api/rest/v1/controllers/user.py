"""
user.py: File, containing twich user endpoints.
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
    DeleteTwichUser,
    DeleteTwichUserByLogin,
    ParseTwichUser,
)
from application.dto import (
    ResultDTO,
    TwichUserDTO,
    TwichUsersDTO,
)
from application.interfaces.bus import (
    ICommandBus,
    IQueryBus,
)
from application.queries import (
    GetAllTwichUsers,
    GetTwichUser,
    GetTwichUserByLogin,
)
from presentation.api.rest.v1.metadata import TwichUserMetadata
from presentation.api.rest.v1.requests import JSONAPIPostSchema
from presentation.api.rest.v1.responses import JSONAPISuccessResponseSchema
from presentation.api.rest.v1.schemas import JSONAPIObjectSchema


class TwichUserCommandController:
    def __init__(self, command_bus: ICommandBus) -> None:
        self.command_bus: ICommandBus = command_bus

        self.router: APIRouter = APIRouter(
            prefix='/twich',
            tags=['twich'],
        )

        self.router.add_api_route(
            path='/user',
            methods=['POST'],
            endpoint=self.parse_user,
            **TwichUserMetadata.parse_user,
        )

        self.router.add_api_route(
            path='/user/{id:int}',
            methods=['DELETE'],
            endpoint=self.delete_user,
            **TwichUserMetadata.delete_user,
        )

        self.router.add_api_route(
            path='/user/{login:str}',
            methods=['DELETE'],
            endpoint=self.delete_user_by_login,
            **TwichUserMetadata.delete_user_by_login,
        )

    async def parse_user(
        self,
        request: Request,
        body: JSONAPIPostSchema,
    ) -> JSONResponse:
        login: str = body.attributes['login']

        command: ParseTwichUser = ParseTwichUser(login=login)
        result: ResultDTO = await self.command_bus.dispatch(command)

        user_id: int = result.data['id']
        resource_url: str = f'{request.url_for("get_user", id=user_id)}'

        links: dict = {
            'self': resource_url,
        }

        response_object: JSONAPIObjectSchema = JSONAPIObjectSchema(
            id=result.data['id'],
            type='user',
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

    async def delete_user(
        self,
        id: Annotated[int, Path(gt=0)],
    ) -> JSONResponse:
        command: DeleteTwichUser = DeleteTwichUser(id=id)
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

    async def delete_user_by_login(
        self,
        login: Annotated[str, Path(min_length=1, max_length=128)],
    ) -> JSONResponse:
        command: DeleteTwichUserByLogin = DeleteTwichUserByLogin(login=login)
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


class TwichUserQueryController:
    def __init__(self, query_bus: IQueryBus) -> None:
        self.query_bus: IQueryBus = query_bus

        self.router: APIRouter = APIRouter(
            prefix='/twich',
            tags=['twich'],
        )

        self.router.add_api_route(
            path='/user/{id:int}',
            methods=['GET'],
            endpoint=self.get_user,
            **TwichUserMetadata.get_user,
        )

        self.router.add_api_route(
            path='/user/{login:str}',
            methods=['GET'],
            endpoint=self.get_user_by_login,
            **TwichUserMetadata.get_user_by_login,
        )

        self.router.add_api_route(
            path='/users',
            methods=['GET'],
            endpoint=self.get_all_users,
            **TwichUserMetadata.get_all_users,
        )

    async def get_user(
        self,
        request: Request,
        id: Annotated[int, Path(gt=0)],
    ) -> JSONResponse:
        query: GetTwichUser = GetTwichUser(id=id)
        user: TwichUserDTO = await self.query_bus.dispatch(query)

        user_attribtutes: dict = asdict(user)
        user_id: int = user_attribtutes.pop('id')

        resource_url: str = f'{request.url_for("get_user", id=user_id)}'

        links: dict = {
            'self': resource_url,
        }

        response_object: JSONAPIObjectSchema = JSONAPIObjectSchema(
            id=user_id,
            type='user',
            attributes=user_attribtutes,
            links=links,
        )

        response: JSONAPISuccessResponseSchema = JSONAPISuccessResponseSchema(
            data=[response_object],
        )

        return JSONResponse(
            content=jsonable_encoder(response),
            status_code=status.HTTP_200_OK,
        )

    async def get_user_by_login(
        self,
        request: Request,
        login: Annotated[str, Path(min_length=1, max_length=128)],
    ) -> JSONResponse:
        query: GetTwichUserByLogin = GetTwichUserByLogin(login=login)
        user: TwichUserDTO = await self.query_bus.dispatch(query)

        user_attribtutes: dict = asdict(user)
        user_id: int = user_attribtutes.pop('id')

        resource_url: str = f'{request.url_for("get_user", id=user_id)}'

        links: dict = {
            'self': resource_url,
        }

        response_object: JSONAPIObjectSchema = JSONAPIObjectSchema(
            id=user_id,
            type='user',
            attributes=user_attribtutes,
            links=links,
        )

        response: JSONAPISuccessResponseSchema = JSONAPISuccessResponseSchema(
            data=[response_object],
        )

        return JSONResponse(
            content=jsonable_encoder(response),
            status_code=status.HTTP_200_OK,
        )

    async def get_all_users(
        self,
        request: Request,
    ) -> JSONResponse:
        query: GetAllTwichUsers = GetAllTwichUsers()
        users: TwichUsersDTO = await self.query_bus.dispatch(query)

        response_objects: list[JSONAPIObjectSchema] = []

        for user in users.data:
            user_attribtutes: dict = asdict(user)
            user_id: int = user_attribtutes.pop('id')

            resource_url: str = f'{request.url_for("get_user", id=user_id)}'

            links: dict = {
                'self': resource_url,
            }

            response_object: JSONAPIObjectSchema = JSONAPIObjectSchema(
                id=user_id,
                type='user',
                attributes=user_attribtutes,
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
