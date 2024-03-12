"""
game.py: File, containing twich game queries.
"""


from dataclasses import dataclass
from application.queries import Query


@dataclass(frozen=True)
class GetTwichGameByName(Query):
    name: str


@dataclass(frozen=True)
class GetAllTwichGames(Query):
    pass
