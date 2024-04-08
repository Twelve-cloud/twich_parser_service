"""
__init__.py: File, containing other exception modules to simplify import.
"""


from application.exceptions.base import ApplicationException
from application.exceptions.common import (
    ObjectNotFoundException,
    ParserException,
    TwichGetObjectBadRequestException,
    TwichRequestTimeoutException,
    TwichRequestUnauthorizedException,
    TwichTokenNotObtainedException,
)


__all__: list[str] = [
    'ApplicationException',
    'ObjectNotFoundException',
    'ParserException',
    'TwichGetObjectBadRequestException',
    'TwichRequestTimeoutException',
    'TwichRequestUnauthorizedException',
    'TwichTokenNotObtainedException',
]
