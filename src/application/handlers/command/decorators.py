"""
decorators.py: File, containing decorators for command handlers.
"""


from typing import Optional

from application.commands import C
from application.dto import ResultDTO
from application.exceptions import ApplicationException
from application.interfaces.handler import (
    ICommandHandler,
    IExceptionHandler,
)
from shared.interfaces import ILogger


class CommandHandlerDecorator(ICommandHandler):
    def __init__(self, command_handler: ICommandHandler) -> None:
        self._command_handler: ICommandHandler = command_handler

    async def handle(self, command: C) -> ResultDTO:
        return await self._command_handler.handle(command)


class ExceptionHandlingDecorator(CommandHandlerDecorator):
    def __init__(
        self,
        command_handler: ICommandHandler,
        exception_handlers: dict[type[ApplicationException], IExceptionHandler],
        logger: ILogger,
    ) -> None:
        super().__init__(command_handler)
        self._exception_handlers: dict[
            type[ApplicationException], IExceptionHandler
        ] = exception_handlers
        self.logger: ILogger = logger

    async def handle(self, command: C) -> ResultDTO:
        try:
            return await super().handle(command)
        except ApplicationException as exc:
            handler: Optional[IExceptionHandler] = self._exception_handlers.get(type(exc))

            if not handler:
                self.logger.critical(str(exc))
                raise exc

            return await handler.handle(exc)
        except Exception as exc:
            self.logger.critical(str(exc))
            raise exc
