"""
__init__.py: File, containing other exception handler modules to simplify import.
"""


from presentation.api.rest.v1.handlers.exception.base import RESTAPIExceptionHandler
from presentation.api.rest.v1.handlers.exception.common import (
    HandleObjectNotFoundException,
    HandleParserException,
    HandleTwichGetObjectBadRequestException,
    HandleTwichRequestTimeoutException,
    HandleTwichRequestUnauthorizedException,
    HandleTwichTokenNotObtainedException,
)


__all__: list[str] = [
    'RESTAPIExceptionHandler',
    'HandleTwichTokenNotObtainedException',
    'HandleTwichRequestUnauthorizedException',
    'HandleTwichGetObjectBadRequestException',
    'HandleParserException',
    'HandleObjectNotFoundException',
    'HandleTwichRequestTimeoutException',
]
