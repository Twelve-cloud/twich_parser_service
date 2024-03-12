"""
game.py: File, containing twich game dto.
"""


from dataclasses import dataclass
from datetime import datetime
from application.dto import BaseDTO


@dataclass(frozen=True)
class TwichGameDTO(BaseDTO):
    id: int
    name: str
    igdb_id: str
    box_art_url: str
    parsed_at: datetime


@dataclass(frozen=True)
class TwichGamesDTO(BaseDTO):
    games: list[TwichGameDTO]
