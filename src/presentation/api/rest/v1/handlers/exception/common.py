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


class HandleTwichTokenNotObtainedException(IExceptionHandler[TwichTokenNotObtainedException]):
    def handle(self, exception: TwichTokenNotObtainedException) -> Any:
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


class HandleTwichRequestUnauthorizedException(IExceptionHandler[TwichRequestUnauthorizedException]):
    def handle(self, exception: TwichRequestUnauthorizedException) -> Any:
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


class HandleTwichGetObjectBadRequestException(IExceptionHandler[TwichGetObjectBadRequestException]):
    def handle(self, exception: TwichGetObjectBadRequestException) -> Any:
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


class HandleTwichRequestTimeoutException(IExceptionHandler[TwichRequestTimeoutException]):
    def handle(self, exception: TwichRequestTimeoutException) -> Any:
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


class HandleObjectNotFoundException(IExceptionHandler[ObjectNotFoundException]):
    def handle(self, exception: ObjectNotFoundException) -> Any:
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


class HandleParserException(IExceptionHandler[ParserException]):
    def handle(self, exception: ParserException) -> Any:
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
