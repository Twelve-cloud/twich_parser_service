"""
base.py: File, containing base domain model.
"""


from abc import ABC
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=False)
class DomainModel(ABC):
    parsed_at: datetime
