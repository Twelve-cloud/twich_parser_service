"""
game.py: File, containing twich game dto.
"""


from dataclasses import dataclass
from datetime import datetime
from application.dto.base import DTO


@dataclass(frozen=True)
class TwichGame(DTO):
    """
    TwichGame: Class, representing twich game dto.

    Bases:
        1) DTO: Base DTO class. Every DTO should be inherited from this class.
    """

    id: int
    name: str
    igdb_id: str
    box_art_url: str
    parsed_at: datetime


@dataclass(frozen=True)
class TwichGames(DTO):
    """
    TwichGames: Class, representing twich games dto.

    Bases:
        1) DTO: Base DTO class. Every DTO should be inherited from this class.
    """

    data: list[TwichGame]
