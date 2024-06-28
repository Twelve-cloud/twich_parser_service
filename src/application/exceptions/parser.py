"""
parser.py: File, containing parser exception.
"""


from dataclasses import dataclass

from application.exceptions.application import ApplicationException


@dataclass(frozen=True)
class ParserException(ApplicationException):
    pass
