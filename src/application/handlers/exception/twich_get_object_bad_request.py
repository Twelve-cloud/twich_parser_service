"""
twich_get_object_bad_request.py: File, containing twich get object bad request exception handler.
"""


from application.exceptions import TwichGetObjectBadRequestException
from application.interfaces.handler import IExceptionHandler
from shared.interfaces import ILogger


class TwichGetObjectBadRequestExceptionHandler(
    IExceptionHandler[TwichGetObjectBadRequestException]
):
    def __init__(self, logger: ILogger) -> None:
        self.logger: ILogger = logger

    async def handle(self, exception: TwichGetObjectBadRequestException) -> None:
        self.logger.warning(exception.message)
        raise exception
