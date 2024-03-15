"""
common.py: File, containing common dto.
"""


from dataclasses import dataclass
from typing import Any
from application.dto.base import DTO


@dataclass(frozen=True)
class Result(DTO):
    """
    Result: Class, representing result DTO.
    It is used to return result (like Failure/Success) from commands.

    Bases:
        1) DTO: Base DTO. Every DTO should be inherited from this class.
    """

    result: list[dict[str, Any]]
