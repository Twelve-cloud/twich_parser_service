"""
twich_request_unauthorized.py: File, containing twich request unauthorized exception handler.
"""


from application.exceptions import TwichRequestUnauthorizedException
from application.interfaces.handler import IExceptionHandler
from shared.interfaces import ILogger


class TwichRequestUnauthorizedExceptionHandler(
    IExceptionHandler[TwichRequestUnauthorizedException]
):
    def __init__(self, logger: ILogger) -> None:
        self.logger: ILogger = logger

    async def handle(self, exception: TwichRequestUnauthorizedException) -> None:
        self.logger.error(exception.message)
        raise exception
