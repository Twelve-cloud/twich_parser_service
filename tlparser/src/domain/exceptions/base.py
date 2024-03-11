"""
base.py: File, containing base domain exception.
"""


from abc import ABC
from dataclasses import dataclass


@dataclass(frozen=True)
class DomainException(Exception, ABC):
    message: str
