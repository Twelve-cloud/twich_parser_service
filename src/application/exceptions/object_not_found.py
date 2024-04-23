"""
object_not_found.py: File, containing object not found exception.
"""


from dataclasses import dataclass

from application.exceptions.application import ApplicationException


@dataclass(frozen=True)
class ObjectNotFoundException(ApplicationException):
    pass
