"""
game.py: File, containing twich game queries.
"""


from dataclasses import dataclass
from application.queries.base import Query


@dataclass(frozen=True)
class GetTwichGame(Query):
    id: int


@dataclass(frozen=True)
class GetTwichGameByName(Query):
    name: str


@dataclass(frozen=True)
class GetAllTwichGames(Query):
    pass
