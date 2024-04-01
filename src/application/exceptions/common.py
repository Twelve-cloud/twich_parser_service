"""
common.py: File, containing common application exceptions.
"""


from dataclasses import dataclass

from application.exceptions.base import ApplicationException


@dataclass(frozen=True)
class TwichTokenNotObtainedException(ApplicationException):
    pass


@dataclass(frozen=True)
class TwichRequestUnauthorizedException(ApplicationException):
    pass


@dataclass(frozen=True)
class TwichGetObjectBadRequestException(ApplicationException):
    pass


@dataclass(frozen=True)
class TwichRequestTimeoutException(ApplicationException):
    pass


@dataclass(frozen=True)
class ObjectNotFoundException(ApplicationException):
    pass


@dataclass(frozen=True)
class ParserException(ApplicationException):
    pass
