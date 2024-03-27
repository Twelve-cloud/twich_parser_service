"""
common.py: File, containing common dto.
"""


from dataclasses import dataclass
from typing import Any
from application.dto.base import DTO


@dataclass(frozen=True)
class ResultDTO(DTO):
    data: dict[str, Any]
    status: str
    description: str
