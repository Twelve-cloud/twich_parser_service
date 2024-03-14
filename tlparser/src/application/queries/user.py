"""
user.py: File, containing twich user queries.
"""


from dataclasses import dataclass
from application.queries.base import Query


@dataclass(frozen=True)
class GetTwichUserByLogin(Query):
    """
    GetTwichUserByLogin: Class, representing get twich user by login query.

    Bases:
        1) Query: Base query. Every query should be inherited from this class.
    """

    login: str


@dataclass(frozen=True)
class GetAllTwichUsers(Query):
    """
    GetAllTwichUsers: Class, representing get all twich users query.

    Bases:
        1) Query: Base query. Every query should be inherited from this class.
    """

    pass
