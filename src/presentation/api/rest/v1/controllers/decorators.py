"""
decorators.py: File, containing decorators for controllers.
"""


from functools import wraps
from inspect import (
    getmembers,
    isbuiltin,
    isfunction,
    ismethod,
)
from typing import (
    Any,
    Callable,
    Optional,
    Union,
)
from uuid import uuid4

from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from application.exceptions import ApplicationException
from application.interfaces.handler import IExceptionHandler
from presentation.api.rest.v1.controllers.game import (
    TwichGameCommandController,
    TwichGameQueryController,
)
from presentation.api.rest.v1.controllers.stream import (
    TwichStreamCommandController,
    TwichStreamQueryController,
)
from presentation.api.rest.v1.controllers.user import (
    TwichUserCommandController,
    TwichUserQueryController,
)
from presentation.api.rest.v1.responses import JSONAPIFailureResponseSchema
from presentation.api.rest.v1.schemas import JSONAPIErrorSchema


ControllerClass = Union[
    TwichGameCommandController,
    TwichGameQueryController,
    TwichStreamCommandController,
    TwichStreamQueryController,
    TwichUserCommandController,
    TwichUserQueryController,
]


class ControllerDecorator:
    def __init__(self, controller: ControllerClass) -> None:
        self._controller: ControllerClass = controller

    def __getattr__(self, name: str) -> Any:
        return getattr(self._controller, name)


class ControllerExceptionHandlingDecorator(ControllerDecorator):
    def __init__(
        self,
        controller: ControllerClass,
        exception_handlers: dict[type[ApplicationException], IExceptionHandler],
    ) -> None:
        super().__init__(controller)
        self._exception_handlers: dict[
            type[ApplicationException], IExceptionHandler
        ] = exception_handlers
        self._decorate_endpoints()

    def _decorate_endpoints(self) -> None:
        for name, member in getmembers(self._controller):
            if (ismethod(member) or isfunction(member)) and not (
                isbuiltin(member) or name.startswith('__')
            ):
                setattr(self._controller, name, self._handling_decorator(member))

    def _get_default_error_response(self, exc: Exception) -> JSONAPIFailureResponseSchema:
        response_error: JSONAPIErrorSchema = JSONAPIErrorSchema(
            id=uuid4().int,
            status='Internal Server Error',
            code='500',
            detail=str(exc),
        )

        response: JSONAPIFailureResponseSchema = JSONAPIFailureResponseSchema(
            errors=[response_error],
        )

        return response

    def _handling_decorator(self, endpoint: Callable) -> Callable:
        @wraps(endpoint)
        async def wrapper(*args: tuple, **kwargs: dict) -> Any:
            try:
                return await endpoint(*args, **kwargs)
            except ApplicationException as exc:
                handler: Optional[IExceptionHandler] = self._exception_handlers.get(type(exc))

                if not handler:
                    return JSONResponse(
                        content=jsonable_encoder(self._get_default_error_response(exc)),
                        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    )

                return await handler.handle(exc)
            except Exception as exc:
                return JSONResponse(
                    content=jsonable_encoder(self._get_default_error_response(exc)),
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        return wrapper
