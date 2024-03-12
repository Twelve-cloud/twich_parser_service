"""
result.py: File, containing command results dto.
"""


from dataclasses import dataclass
from application.dto import DTO


@dataclass(frozen=True)
class Success(DTO):
    status: str


@dataclass(frozen=True)
class Failure(DTO):
    status: str
