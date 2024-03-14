"""
common.py: File, containing common things related to dto.
"""


from dataclasses import dataclass
from typing import Any, TypeVar
from application.dto.base import DTO


RD = TypeVar('RD', bound=DTO)


@dataclass(frozen=True)
class Result(DTO):
    """
    Result: Class, representing result DTO.
    It is used to return result (like Failure/Success) from commands.

    Bases:
        1) DTO: Base DTO. Every DTO should be inherited from this class.
    """

    result: list[dict[str, Any]]
