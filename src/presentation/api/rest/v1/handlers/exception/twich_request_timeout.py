"""
twich_request_timeout.py: File, containing twich request timeout exception handler.
"""


from uuid import uuid4

from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from application.exceptions import TwichRequestTimeoutException
from application.interfaces.handler import IExceptionHandler
from presentation.api.rest.v1.responses import JSONAPIFailureResponseSchema
from presentation.api.rest.v1.schemas import JSONAPIErrorSchema


class TwichRequestTimeoutExceptionHandler(IExceptionHandler[TwichRequestTimeoutException]):
    async def handle(self, exception: TwichRequestTimeoutException) -> JSONResponse:
        response_error: JSONAPIErrorSchema = JSONAPIErrorSchema(
            id=uuid4().int,
            status='Service Unavailable',
            code='503',
            detail=str(exception),
        )

        response: JSONAPIFailureResponseSchema = JSONAPIFailureResponseSchema(
            errors=[response_error],
        )

        return JSONResponse(
            content=jsonable_encoder(response),
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        )
