"""
twich_request_timeout.py: File, containing twich request timeout exception.
"""


from dataclasses import dataclass

from application.exceptions.application import ApplicationException


@dataclass(frozen=True)
class TwichRequestTimeoutException(ApplicationException):
    pass
