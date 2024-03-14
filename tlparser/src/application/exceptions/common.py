"""
common.py: File, containing common things related to application exceptions.
"""


from dataclasses import dataclass
from application.exceptions.base import ApplicationException


@dataclass(frozen=True)
class TwichTokenNotObtainedException(ApplicationException):
    """
    TwichTokenNotObtainedException: Class, representing twich token not obtained exception.
    This exception occurs when the process of gettings token has failed.

    Bases:
        1) ApplicationException: Base application exception.
           Every application exception should be inherited from this class.
    """

    pass


@dataclass(frozen=True)
class TwichRequestUnauthorizedException(ApplicationException):
    """
    TwichRequestUnauthorizedException: Class, representing twich request unauthorized exception.
    This exception occurs when the request to twich does not have Authorization header.

    Bases:
        1) ApplicationException: Base application exception.
           Every application exception should be inherited from this class.
    """

    pass


@dataclass(frozen=True)
class TwichGetObjectBadRequestException(ApplicationException):
    """
    TwichGetObjectBadRequestException: Class, representing twich get object bad request exception.
    This exception occurs when the reuqest to twich returns bad request error.

    Bases:
        1) ApplicationException: Base application exception.
           Every application exception should be inherited from this class.
    """

    pass


@dataclass(frozen=True)
class TwichRequestTimeoutException(ApplicationException):
    """
    TwichRequestTimeoutException: Class, representing twich request timeout exception.
    This exception occurs when the request to twich has timed out.

    Bases:
        1) ApplicationException: Base application exception.
           Every application exception should be inherited from this class.
    """

    pass


@dataclass(frozen=True)
class ObjectNotFoundException(ApplicationException):
    """
    ObjectNotFoundException: Class, representing object not found exception.
    This exception occurs when object is not found while parsing or gettings from db.


    Bases:
        1) ApplicationException: Base application exception.
           Every application exception should be inherited from this class.
    """

    pass


@dataclass(frozen=True)
class ParserException(ApplicationException):
    """
    ParserException: Class, representing parser exception.
    This exception occurs when parser implementation has critical errors.

    Bases:
        1) ApplicationException: Base application exception.
           Every application exception should be inherited from this class.
    """

    pass
