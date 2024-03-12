"""
result.py: File, containing command results dto.
"""


from dataclasses import dataclass
from application.dto import DTO


@dataclass(frozen=True)
class SuccessDTO(DTO):
    status: str


@dataclass(frozen=True)
class FailureDTO(DTO):
    status: str
