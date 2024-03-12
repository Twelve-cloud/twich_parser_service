"""
game.py: File, containing twich game queries.
"""


from dataclasses import dataclass
from application.queries import BaseQuery


@dataclass(frozen=True)
class GetTwichGameByNameQuery(BaseQuery):
    name: str


@dataclass(frozen=True)
class GetAllTwichGamesQuery(BaseQuery):
    pass
