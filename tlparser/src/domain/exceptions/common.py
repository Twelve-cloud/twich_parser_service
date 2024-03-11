"""
common.py: File, containing common domain exceptions.
"""


from dataclasses import dataclass
from domain.exceptions import DomainException


@dataclass(frozen=True)
class TwichTokenNotObtainedException(DomainException):
    pass


@dataclass(frozen=True)
class TwichRequestUnauthorizedException(DomainException):
    pass


@dataclass(frozen=True)
class TwichGetObjectBadRequestException(DomainException):
    pass


@dataclass(frozen=True)
class TwichRequestTimeoutException(DomainException):
    pass


@dataclass(frozen=True)
class ObjectNotFoundException(DomainException):
    pass


@dataclass(frozen=True)
class ParserException(DomainException):
    pass
