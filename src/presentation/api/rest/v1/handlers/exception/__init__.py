"""
__init__.py: File, containing other exception handler modules to simplify import.
"""


from presentation.api.rest.v1.handlers.exception.base import RESTAPIExceptionHandler
from presentation.api.rest.v1.handlers.exception.common import (
    ObjectNotFoundExceptionHandler,
    ParserExceptionHandler,
    TwichGetObjectBadRequestExceptionHandler,
    TwichRequestTimeoutExceptionHandler,
    TwichRequestUnauthorizedExceptionHandler,
    TwichTokenNotObtainedExceptionHandler,
)


__all__: list[str] = [
    'RESTAPIExceptionHandler',
    'ObjectNotFoundExceptionHandler',
    'ParserExceptionHandler',
    'TwichGetObjectBadRequestExceptionHandler',
    'TwichRequestTimeoutExceptionHandler',
    'TwichRequestUnauthorizedExceptionHandler',
    'TwichTokenNotObtainedExceptionHandler',
]
