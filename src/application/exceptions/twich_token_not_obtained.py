"""
twich_token_not_obtained.py: File, containing twich token not obtained exception.
"""


from dataclasses import dataclass

from application.exceptions.application import ApplicationException


@dataclass(frozen=True)
class TwichTokenNotObtainedException(ApplicationException):
    pass
