"""
twich_get_object_bad_request.py: File, containing twich get object bad request exception.
"""


from dataclasses import dataclass

from application.exceptions.application import ApplicationException


@dataclass(frozen=True)
class TwichGetObjectBadRequestException(ApplicationException):
    pass
