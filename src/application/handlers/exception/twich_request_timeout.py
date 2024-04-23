"""
twich_request_timeout.py: File, containing twich request timeout exception handler.
"""


from application.exceptions import TwichRequestTimeoutException
from application.interfaces.handler import IExceptionHandler
from shared.interfaces import ILogger


class TwichRequestTimeoutExceptionHandler(IExceptionHandler[TwichRequestTimeoutException]):
    def __init__(self, logger: ILogger) -> None:
        self.logger: ILogger = logger

    async def handle(self, exception: TwichRequestTimeoutException) -> None:
        self.logger.error(exception.message)
        raise exception
