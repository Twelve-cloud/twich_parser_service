"""
__init__.py: File, containing other exception modules to simplify import.
"""


from typing import TypeVar

from application.exceptions.application import ApplicationException
from application.exceptions.object_not_found import ObjectNotFoundException
from application.exceptions.parser import ParserException
from application.exceptions.twich_get_object_bad_request import TwichGetObjectBadRequestException
from application.exceptions.twich_request_timeout import TwichRequestTimeoutException
from application.exceptions.twich_request_unauthorized import TwichRequestUnauthorizedException
from application.exceptions.twich_token_not_obtained import TwichTokenNotObtainedException


E = TypeVar('E', bound=ApplicationException)


__all__: list[str] = [
    'ApplicationException',
    'ObjectNotFoundException',
    'ParserException',
    'TwichGetObjectBadRequestException',
    'TwichRequestTimeoutException',
    'TwichRequestUnauthorizedException',
    'TwichTokenNotObtainedException',
]
