"""
base.py: File, containing base query.
"""


from abc import ABC
from dataclasses import dataclass


@dataclass(frozen=True)
class BaseQuery(ABC):
    pass
