"""
__init__.py: File, containing other exception handler modules to simplify import.
"""


from application.handlers.exception.object_not_found import ObjectNotFoundExceptionHandler
from application.handlers.exception.parser import ParserExceptionHandler
from application.handlers.exception.twich_get_object_bad_request import (
    TwichGetObjectBadRequestExceptionHandler,
)
from application.handlers.exception.twich_request_timeout import TwichRequestTimeoutExceptionHandler
from application.handlers.exception.twich_request_unauthorized import (
    TwichRequestUnauthorizedExceptionHandler,
)
from application.handlers.exception.twich_token_not_obtained import (
    TwichTokenNotObtainedExceptionHandler,
)


__all__: list[str] = [
    'ObjectNotFoundExceptionHandler',
    'ParserExceptionHandler',
    'TwichGetObjectBadRequestExceptionHandler',
    'TwichRequestTimeoutExceptionHandler',
    'TwichRequestUnauthorizedExceptionHandler',
    'TwichTokenNotObtainedExceptionHandler',
]
