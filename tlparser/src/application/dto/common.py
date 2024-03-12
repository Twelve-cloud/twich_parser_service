"""
common.py: File, containing common dto.
"""


from dataclasses import dataclass
from typing import Any
from application.dto import DTO


@dataclass(frozen=True)
class Result(DTO):
    result: list[dict[str, Any]]
