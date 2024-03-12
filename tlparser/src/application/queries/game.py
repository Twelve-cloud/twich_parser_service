"""
game.py: File, containing twich game queries.
"""


from dataclasses import dataclass
from application.queries import Query


@dataclass(frozen=True)
class GetTwichGameByNameQuery(Query):
    name: str


@dataclass(frozen=True)
class GetAllTwichGamesQuery(Query):
    pass
