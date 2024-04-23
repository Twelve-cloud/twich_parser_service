"""
twich_request_unauthorized.py: File, containing twich request unauthorized exception.
"""


from dataclasses import dataclass

from application.exceptions.application import ApplicationException


@dataclass(frozen=True)
class TwichRequestUnauthorizedException(ApplicationException):
    pass
