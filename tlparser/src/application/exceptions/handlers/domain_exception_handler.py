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
    BaseDomainException,
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
            logger (ILogger): Logger interface.
        """

        self.logger: ILogger = logger

        self.handler_map: dict[type[BaseDomainException], Callable] = {
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
            raise ServiceUnavailableException(exception.message)

    def handle_token_exception(self, exception: TwichTokenNotObtainedException) -> None:
        """
        handle_token_exception: Handle twich token not obtained exception.

        Args:
            exception (TwichTokenNotObtainedException): Twich token not obtained exception.

        Raises:
            ServiceUnavailableException: Service unavailable exception.
        """

        raise TwichException(message=exception.message)

    def handle_unauthorized_exception(self, exception: TwichRequestUnauthorizedException) -> None:
        """
        handle_unauthorized_exception: Handle twich request unauthorized exception.

        Args:
            exception (TwichRequestUnauthorizedException): Twich request unauthorized exception.

        Raises:
            ServiceUnavailableException: Service unavailable exception.
        """

        raise TwichException(message=exception.message)

    def handle_bad_request_exception(self, exception: GetObjectBadRequestException) -> None:
        """
        handle_bad_request_exception _summary_

        Args:
            exception (GetObjectBadRequestException): _description_
        """

        raise TwichException(message=exception.message)

    def handle_timeout_exception(self, exception: TwichRequestTimeoutException) -> None:
        """
        handle_timeout_exception: Handle timeout error by asyncio.

        Args:
            exception (TimeoutError): Timeout error.

        Raises:
            RequestTimeoutException: Request timeout exception.
        """

        raise RequestTimeoutException(message=exception.message)

    def handle_not_found_exception(self, exception: ObjectNotFoundException) -> None:
        """
        handle_not_found_exception _summary_

        Args:
            exception (ObjectNotFoundException): _description_
        """

        raise NotFoundException(message=exception.message)

    def handle_parser_exception(self, exception: ParserException) -> None:
        """
        handle_parser_exception: Handle client error by aiohttp.

        Args:
            exception (ClientError): Client error.

        Raises:
            ServiceUnavailableException: Service unavailable exception.
        """

        raise ServiceUnavailableException(message=exception.message)
