# """
# user.py: File, containing endpoinds for a twich user.
# """


# from typing import Annotated
# from dependency_injector.wiring import Provide, inject
# from fastapi import APIRouter, Depends, Path, Response, status
# from fastapi.responses import JSONResponse
# from application.dtos.fastapi_schemas.twich.user_schema import TwichUserSchema
# from application.services.decorators import ServiceDecorator
# from container import Container
# from presentation.api.rest.v1.v1.metadata.twich.user_metadata import TwichUserMetadata


# # from fastapi_cache.decorator import cache


# router: APIRouter = APIRouter(
#     prefix='/twich',
#     tags=['twich'],
# )


# @router.get(
#     path='/private/user/{user_login}',
#     status_code=status.HTTP_200_OK,
#     **TwichUserMetadata.private_parse_user,
# )
# # @cache(60)
# @inject
# async def private_parse_user(
#     user_login: Annotated[str, Path(min_length=1, max_length=128)],
#     service_decorator: ServiceDecorator = Depends(
#         Provide[Container.twich_user_w_service_decorator]
#     ),
# ) -> TwichUserSchema:
#     """
#     private_parse_user: Parse twich user and return result as TwichUserSchema.

#     Args:
#         user_login (str): Login of the user.
#         service_decorator (ServiceDecorator): Twich user service_decorator.

#     Returns:
#         TwichUserSchema: Response as TwichUserSchema instance.
#     """

#     return await service_decorator.private_parse_user(user_login)


# @router.delete(
#     path='/user/{user_login}',
#     status_code=status.HTTP_204_NO_CONTENT,
#     **TwichUserMetadata.delete_user_by_login,
# )
# @inject
# async def delete_user_by_login(
#     user_login: Annotated[str, Path(min_length=1, max_length=128)],
#     service_decorator: ServiceDecorator = Depends(
#         Provide[Container.twich_user_w_service_decorator]
#     ),
# ) -> Response:
#     """
#     delete_user_by_login: Delete twich user.

#     Args:
#         user_login (str): Login of the user.
#         service_decorator (ServiceDecorator): Twich user service_decorator.

#     Returns:
#         Response: HTTP status code 204.
#     """

#     await service_decorator.delete_user_by_login(user_login)

#     return Response(status_code=status.HTTP_204_NO_CONTENT)


# @router.get(
#     path='/users',
#     status_code=status.HTTP_200_OK,
#     **TwichUserMetadata.get_all_users,
# )
# # @cache(expire=60)
# @inject
# async def get_all_users(
#     service_decorator: ServiceDecorator = Depends(
#         Provide[Container.twich_user_r_service_decorator]
#     ),
# ) -> list[TwichUserSchema]:
#     """
#     get_all_users: Return all twich users.

#     Args:
#         service_decorator (ServiceDecorator): Twich user service_decorator.

#     Returns:
#         list[TwichUserSchema]: List of twich users.
#     """

#     return await service_decorator.get_all_users()


# @router.get(
#     path='/user/{user_login}',
#     status_code=status.HTTP_200_OK,
#     **TwichUserMetadata.get_user_by_login,
# )
# # @cache(expire=60)
# @inject
# async def get_user_by_login(
#     user_login: Annotated[str, Path(min_length=1, max_length=128)],
#     service_decorator: ServiceDecorator = Depends(
#         Provide[Container.twich_user_r_service_decorator]
#     ),
# ) -> TwichUserSchema:
#     """
#     get_user_by_login: Return twich user by login.

#     Args:
#         user_login (str): Login of the user.
#         service_decorator (ServiceDecorator): Twich user service_decorator.

#     Returns:
#         TwichUserSchema: TwichUserSchema instance.
#     """

#     return await service_decorator.get_user_by_login(user_login)
