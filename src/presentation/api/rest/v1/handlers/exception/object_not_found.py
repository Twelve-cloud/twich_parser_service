"""
object_not_found.py: File, containing object not found exception handler.
"""


from uuid import uuid4

from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from application.exceptions import ObjectNotFoundException
from application.interfaces.handler import IExceptionHandler
from presentation.api.rest.v1.responses import JSONAPIFailureResponseSchema
from presentation.api.rest.v1.schemas import JSONAPIErrorSchema


class ObjectNotFoundExceptionHandler(IExceptionHandler[ObjectNotFoundException]):
    async def handle(self, exception: ObjectNotFoundException) -> JSONResponse:
        response_error: JSONAPIErrorSchema = JSONAPIErrorSchema(
            id=uuid4().int,
            status='Not Found',
            code='404',
            detail=str(exception),
        )

        response: JSONAPIFailureResponseSchema = JSONAPIFailureResponseSchema(
            errors=[response_error],
        )

        return JSONResponse(
            content=jsonable_encoder(response),
            status_code=status.HTTP_404_NOT_FOUND,
        )
