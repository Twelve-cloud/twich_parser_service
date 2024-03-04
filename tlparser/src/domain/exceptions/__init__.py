"""
__init__.py: File, containing other exception modules to simplify import.
"""


from domain.exceptions.base import BaseDomainException
from domain.exceptions.common import (
    ObjectNotFoundException,
    ParserException,
    TwichGetObjectBadRequestException,
    TwichRequestTimeoutException,
    TwichRequestUnauthorizedException,
    TwichTokenNotObtainedException,
)


__all__: list[str] = [
    'BaseDomainException',
    'ObjectNotFoundException',
    'ParserException',
    'TwichGetObjectBadRequestException',
    'TwichRequestTimeoutException',
    'TwichRequestUnauthorizedException',
    'TwichTokenNotObtainedException',
]
