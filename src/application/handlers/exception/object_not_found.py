"""
object_not_found.py: File, containing object not found exception handler.
"""


from application.exceptions import ObjectNotFoundException
from application.interfaces.handler import IExceptionHandler
from shared.interfaces import ILogger


class ObjectNotFoundExceptionHandler(IExceptionHandler[ObjectNotFoundException]):
    def __init__(self, logger: ILogger) -> None:
        self.logger: ILogger = logger

    async def handle(self, exception: ObjectNotFoundException) -> None:
        self.logger.error(exception.message)
        raise exception
