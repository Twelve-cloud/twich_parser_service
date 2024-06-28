"""
parser.py: File, containing parser exception handler.
"""


from uuid import uuid4

from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from application.exceptions import ParserException
from application.interfaces.handler import IExceptionHandler
from presentation.api.rest.v1.responses import JSONAPIFailureResponseSchema
from presentation.api.rest.v1.schemas import JSONAPIErrorSchema


class ParserExceptionHandler(IExceptionHandler[ParserException]):
    async def handle(self, exception: ParserException) -> JSONResponse:
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
