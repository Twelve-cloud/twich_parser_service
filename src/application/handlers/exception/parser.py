"""
parser.py: File, containing parser exception handler.
"""


from application.exceptions import ParserException
from application.interfaces.handler import IExceptionHandler
from shared.interfaces import ILogger


class ParserExceptionHandler(IExceptionHandler[ParserException]):
    def __init__(self, logger: ILogger) -> None:
        self.logger: ILogger = logger

    async def handle(self, exception: ParserException) -> None:
        self.logger.critical(exception.message)
        raise exception
