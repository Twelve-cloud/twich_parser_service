"""
result.py: File, containing command results dto.
"""


from dataclasses import dataclass
from application.dto import BaseDTO


@dataclass(frozen=True)
class SuccessDTO(BaseDTO):
    status: str


@dataclass(frozen=True)
class FailureDTO(BaseDTO):
    status: str
