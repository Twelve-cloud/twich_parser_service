"""
base.py: File, containing base exception handler for rest api.
"""


from functools import wraps
from typing import (
    Any,
    Callable,
    Optional,
)
from uuid import uuid4

from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from presentation.api.rest.v1.responses import JSONAPIFailureResponseSchema
from presentation.api.rest.v1.schemas import JSONAPIErrorSchema
from shared.interfaces import IExceptionHandler


class RESTAPIExceptionHandler:
    def __init__(self) -> None:
        self._handlers: dict[type[Exception], IExceptionHandler] = {}

    def __call__(self, endpoint: Callable) -> Callable:
        @wraps(endpoint)
        async def wrapper(*args: tuple, **kwargs: dict) -> Any:
            try:
                return await endpoint(*args, **kwargs)
            except Exception as exc:
                handler: Optional[IExceptionHandler] = self._handlers.get(type(exc))

                if not handler:
                    response_error: JSONAPIErrorSchema = JSONAPIErrorSchema(
                        id=uuid4().int,
                        status='Internal Server Error',
                        code='500',
                        detail=str(exc),
                    )

                    response: JSONAPIFailureResponseSchema = JSONAPIFailureResponseSchema(
                        errors=[response_error],
                    )

                    return JSONResponse(
                        content=jsonable_encoder(response),
                        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    )

                handler.handle(exc)

        return wrapper

    def register(self, exc_class: type[Exception], exc_handler: IExceptionHandler) -> None:
        if exc_class not in self._handlers:
            self._handlers[exc_class] = exc_handler
        else:
            raise Exception('Exception handler has been already registered.')
