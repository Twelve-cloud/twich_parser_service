"""
game.py: File, containing twich game dto.
"""


from dataclasses import dataclass
from datetime import datetime
from application.dto.base import DTO


@dataclass(frozen=True)
class TwichGame(DTO):
    id: int
    name: str
    igdb_id: str
    box_art_url: str
    parsed_at: datetime


@dataclass(frozen=True)
class TwichGames(DTO):
    data: list[TwichGame]
