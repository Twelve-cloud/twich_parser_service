"""
domain_exception_handler.py: File, containing domain exception handler.
"""


from typing import Callable, Optional
from application.exceptions import (
    NotFoundException,
    RequestTimeoutException,
    ServiceUnavailableException,
    TwichException,
)
from common.interfaces import IExceptionHandler, ILogger
from domain.exceptions import (
    ObjectNotFoundException,
    ParserException,
    TwichGetObjectBadRequestException,
    TwichRequestTimeoutException,
    TwichRequestUnauthorizedException,
    TwichTokenNotObtainedException,
)


class DomainExceptionHandler(IExceptionHandler):
    """
    DomainExceptionHandler: Class, that represents domain exception handler.

    Args:
        IExceptionHandler: Exception handler interface.
    """

    def __init__(self, logger: ILogger) -> None:
        """
        __init__: Initialize domain exception handler.

        Args:
            logger (ILogger): Logger.
        """

        self.logger: ILogger = logger

        self.handler_map: dict[type[Exception], Callable] = {
            ObjectNotFoundException: self.handle_not_found_exception,
            ParserException: self.handle_parser_exception,
            TwichGetObjectBadRequestException: self.handle_bad_request_exception,
            TwichRequestTimeoutException: self.handle_timeout_exception,
            TwichRequestUnauthorizedException: self.handle_unauthorized_exception,
            TwichTokenNotObtainedException: self.handle_token_exception,
        }

    def handle(self, exception: Exception) -> None:
        """
        handle: Handle exceptions by calling more specific handlers.

        Args:
            exception (Exception): Exception that should be handled.

        Raises:
            ServiceUnavailableException: Service unavailable exception.
        """

        handler: Optional[Callable] = self.handler_map.get(type(exception))

        if handler:
            handler(exception)
        else:
            self.logger.log(self.logger.CRITICAL, str(exception))
            raise ServiceUnavailableException(str(exception))

    def handle_not_found_exception(self, exception: ObjectNotFoundException) -> None:
        """
        handle_not_found_exception: Handle object not found exception.

        Args:
            exception (ObjectNotFoundException): Object not found exception.

        Raises:
            NotFoundException: Not found exception.
        """

        self.logger.log(self.logger.ERROR, exception.message)
        raise NotFoundException(exception.message)

    def handle_parser_exception(self, exception: ParserException) -> None:
        """
        handle_parser_exception: Handle parser exception.

        Args:
            exception (ParserException): Parser exception.

        Raises:
            ServiceUnavailableException: Service unavailable exception.
        """

        self.logger.log(self.logger.CRITICAL, exception.message)
        raise ServiceUnavailableException(exception.message)

    def handle_bad_request_exception(self, exception: TwichGetObjectBadRequestException) -> None:
        """
        handle_bad_request_exception: Handle twich get object bad request exception.

        Args:
            exception (TwichGetObjectBadRequestException): Twich get object bad request exception.

        Raises:
            TwichException: Twich exception.
        """

        self.logger.log(self.logger.CRITICAL, exception.message)
        raise TwichException(exception.message)

    def handle_timeout_exception(self, exception: TwichRequestTimeoutException) -> None:
        """
        handle_timeout_exception: Handle twich request timeout exception.

        Args:
            exception (TwichRequestTimeoutException): Twich request timeout exception.

        Raises:
            RequestTimeoutException: Request timeout exception.
        """

        self.logger.log(self.logger.ERROR, exception.message)
        raise RequestTimeoutException(exception.message)

    def handle_unauthorized_exception(self, exception: TwichRequestUnauthorizedException) -> None:
        """
        handle_unauthorized_exception: Handle twich request unauthorized exception.

        Args:
            exception (TwichRequestUnauthorizedException): Twich request unauthorized exception.

        Raises:
            TwichException: Twich exception.
        """

        self.logger.log(self.logger.CRITICAL, exception.message)
        raise TwichException(exception.message)

    def handle_token_exception(self, exception: TwichTokenNotObtainedException) -> None:
        """
        handle_token_exception: Handle twich token not obtained exception.

        Args:
            exception (TwichTokenNotObtainedException): Twich token not obtained exception.

        Raises:
            TwichException: Twich exception.
        """

        self.logger.log(self.logger.CRITICAL, exception.message)
        raise TwichException(exception.message)
