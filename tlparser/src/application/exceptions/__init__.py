"""
__init__.py: File, containing other exception modules to simplify import.
"""


from application.exceptions.base import BaseApplicationException
from application.exceptions.common import (
    NotFoundException,
    RequestTimeoutException,
    ServiceUnavailableException,
    TwichException,
)


__all__: list[str] = [
    'BaseApplicationException',
    'NotFoundException',
    'RequestTimeoutException',
    'ServiceUnavailableException',
    'TwichException',
]
