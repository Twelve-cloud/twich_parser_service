"""
decorators.py: File, containing decorators for command handlers.
"""


from typing import Optional

from application.dto import RD
from application.exceptions import ApplicationException
from application.interfaces.handler import (
    IExceptionHandler,
    IQueryHandler,
)
from application.queries import Q
from shared.interfaces import ILogger


class QueryHandlerDecorator(IQueryHandler):
    def __init__(self, query_handler: IQueryHandler) -> None:
        self._query_handler: IQueryHandler = query_handler

    async def handle(self, query: Q) -> RD:
        return await self._query_handler.handle(query)


class ExceptionHandlingDecorator(QueryHandlerDecorator):
    def __init__(
        self,
        query_handler: IQueryHandler,
        exception_handlers: dict[type[ApplicationException], IExceptionHandler],
        logger: ILogger,
    ) -> None:
        super().__init__(query_handler)
        self._exception_handlers: dict[
            type[ApplicationException], IExceptionHandler
        ] = exception_handlers
        self.logger: ILogger = logger

    async def handle(self, query: Q) -> RD:
        try:
            return await super().handle(query)
        except ApplicationException as exc:
            handler: Optional[IExceptionHandler] = self._exception_handlers.get(type(exc))

            if not handler:
                self.logger.critical(str(exc))
                raise exc

            return await handler.handle(exc)
        except Exception as exc:
            self.logger.critical(str(exc))
            raise exc
