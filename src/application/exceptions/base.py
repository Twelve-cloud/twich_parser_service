"""
base.py: File, containing base application exception.
"""


from abc import ABC
from dataclasses import dataclass


@dataclass(frozen=True)
class ApplicationException(Exception, ABC):
    message: str
