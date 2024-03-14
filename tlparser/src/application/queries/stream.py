"""
game.py: File, containing twich stream queries.
"""


from dataclasses import dataclass
from application.queries.base import Query


@dataclass(frozen=True)
class GetTwichStreamByUserLogin(Query):
    """
    GetTwichStreamByUserLogin: Class, representing get twich stream by user login query.

    Bases:
        1) Query: Base query class. Every query should be inherited from this class.
    """

    user_login: str


@dataclass(frozen=True)
class GetAllTwichStreams(Query):
    """
    GetAllTwichStreams: Class, representing get all twich streams query.

    Bases:
        1) Query: Base query class. Every query should be inherited from this class.
    """

    pass
