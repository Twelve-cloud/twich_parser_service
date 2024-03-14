"""
game.py: File, containing twich game queries.
"""


from dataclasses import dataclass
from application.queries.base import Query


@dataclass(frozen=True)
class GetTwichGameByName(Query):
    """
    GetTwichGameByName: Class, representing get twich game by name query.

    Bases:
        1) Query: Base query. Every query should be inherited from this class.
    """

    name: str


@dataclass(frozen=True)
class GetAllTwichGames(Query):
    """
    GetAllTwichGames: Class, representing get all twich games query.

    Bases:
        1) Query: Base query. Every query should be inherited from this class.
    """

    pass
