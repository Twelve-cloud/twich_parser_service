"""
twich_token_not_obtained.py: File, containing twich token not obtained exception handler.
"""


from application.exceptions import TwichTokenNotObtainedException
from application.interfaces.handler import IExceptionHandler
from shared.interfaces import ILogger


class TwichTokenNotObtainedExceptionHandler(IExceptionHandler[TwichTokenNotObtainedException]):
    def __init__(self, logger: ILogger) -> None:
        self.logger: ILogger = logger

    async def handle(self, exception: TwichTokenNotObtainedException) -> None:
        self.logger.error(exception.message)
        raise exception
