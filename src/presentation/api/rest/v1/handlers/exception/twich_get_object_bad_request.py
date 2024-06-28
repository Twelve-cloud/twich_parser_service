"""
twich_get_object_bad_request.py: File, containing twich get object bad request exception handler.
"""


from uuid import uuid4

from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from application.exceptions import TwichGetObjectBadRequestException
from application.interfaces.handler import IExceptionHandler
from presentation.api.rest.v1.responses import JSONAPIFailureResponseSchema
from presentation.api.rest.v1.schemas import JSONAPIErrorSchema


class TwichGetObjectBadRequestExceptionHandler(
    IExceptionHandler[TwichGetObjectBadRequestException]
):
    async def handle(self, exception: TwichGetObjectBadRequestException) -> JSONResponse:
        response_error: JSONAPIErrorSchema = JSONAPIErrorSchema(
            id=uuid4().int,
            status='Internal Server Error',
            code='500',
            detail=str(exception),
        )

        response: JSONAPIFailureResponseSchema = JSONAPIFailureResponseSchema(
            errors=[response_error],
        )

        return JSONResponse(
            content=jsonable_encoder(response),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
