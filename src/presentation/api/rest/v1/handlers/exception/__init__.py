"""
__init__.py: File, containing other exception handler modules to simplify import.
"""


from presentation.api.rest.v1.handlers.exception.object_not_found import (
    ObjectNotFoundExceptionHandler,
)
from presentation.api.rest.v1.handlers.exception.parser import ParserExceptionHandler
from presentation.api.rest.v1.handlers.exception.twich_get_object_bad_request import (
    TwichGetObjectBadRequestExceptionHandler,
)
from presentation.api.rest.v1.handlers.exception.twich_request_timeout import (
    TwichRequestTimeoutExceptionHandler,
)
from presentation.api.rest.v1.handlers.exception.twich_request_unauthorized import (
    TwichRequestUnauthorizedExceptionHandler,
)
from presentation.api.rest.v1.handlers.exception.twich_token_not_obtained import (
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
