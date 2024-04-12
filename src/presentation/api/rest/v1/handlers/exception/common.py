"""
common.py: File, containing specific exception handlers for rest api.
"""


from typing import Any
from uuid import uuid4

from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from application.exceptions.common import (
    ObjectNotFoundException,
    ParserException,
    TwichGetObjectBadRequestException,
    TwichRequestTimeoutException,
    TwichRequestUnauthorizedException,
    TwichTokenNotObtainedException,
)
from presentation.api.rest.v1.responses import JSONAPIFailureResponseSchema
from presentation.api.rest.v1.schemas import JSONAPIErrorSchema
from shared.interfaces import IExceptionHandler


class TwichTokenNotObtainedExceptionHandler(IExceptionHandler[TwichTokenNotObtainedException]):
    async def handle(self, exception: TwichTokenNotObtainedException) -> Any:
        response_error: JSONAPIErrorSchema = JSONAPIErrorSchema(
            id=uuid4().int,
            status='Internal Server Error',
            code='500',
            detail=exception.message,
        )

        response: JSONAPIFailureResponseSchema = JSONAPIFailureResponseSchema(
            errors=[response_error],
        )

        return JSONResponse(
            content=jsonable_encoder(response),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


class TwichRequestUnauthorizedExceptionHandler(
    IExceptionHandler[TwichRequestUnauthorizedException]
):
    async def handle(self, exception: TwichRequestUnauthorizedException) -> Any:
        response_error: JSONAPIErrorSchema = JSONAPIErrorSchema(
            id=uuid4().int,
            status='Internal Server Error',
            code='500',
            detail=exception.message,
        )

        response: JSONAPIFailureResponseSchema = JSONAPIFailureResponseSchema(
            errors=[response_error],
        )

        return JSONResponse(
            content=jsonable_encoder(response),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


class TwichGetObjectBadRequestExceptionHandler(
    IExceptionHandler[TwichGetObjectBadRequestException]
):
    async def handle(self, exception: TwichGetObjectBadRequestException) -> Any:
        response_error: JSONAPIErrorSchema = JSONAPIErrorSchema(
            id=uuid4().int,
            status='Internal Server Error',
            code='500',
            detail=exception.message,
        )

        response: JSONAPIFailureResponseSchema = JSONAPIFailureResponseSchema(
            errors=[response_error],
        )

        return JSONResponse(
            content=jsonable_encoder(response),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


class TwichRequestTimeoutExceptionHandler(IExceptionHandler[TwichRequestTimeoutException]):
    async def handle(self, exception: TwichRequestTimeoutException) -> Any:
        response_error: JSONAPIErrorSchema = JSONAPIErrorSchema(
            id=uuid4().int,
            status='Service Unavailable',
            code='503',
            detail=exception.message,
        )

        response: JSONAPIFailureResponseSchema = JSONAPIFailureResponseSchema(
            errors=[response_error],
        )

        return JSONResponse(
            content=jsonable_encoder(response),
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        )


class ObjectNotFoundExceptionHandler(IExceptionHandler[ObjectNotFoundException]):
    async def handle(self, exception: ObjectNotFoundException) -> Any:
        response_error: JSONAPIErrorSchema = JSONAPIErrorSchema(
            id=uuid4().int,
            status='Not Found',
            code='404',
            detail=exception.message,
        )

        response: JSONAPIFailureResponseSchema = JSONAPIFailureResponseSchema(
            errors=[response_error],
        )

        return JSONResponse(
            content=jsonable_encoder(response),
            status_code=status.HTTP_404_NOT_FOUND,
        )


class ParserExceptionHandler(IExceptionHandler[ParserException]):
    async def handle(self, exception: ParserException) -> Any:
        response_error: JSONAPIErrorSchema = JSONAPIErrorSchema(
            id=uuid4().int,
            status='Internal Server Error',
            code='500',
            detail=exception.message,
        )

        response: JSONAPIFailureResponseSchema = JSONAPIFailureResponseSchema(
            errors=[response_error],
        )

        return JSONResponse(
            content=jsonable_encoder(response),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
