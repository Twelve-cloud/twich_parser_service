"""
user.py: File, containing twich user queries.
"""


from dataclasses import dataclass
from application.queries.base import Query


@dataclass(frozen=True)
class GetTwichUser(Query):
    id: int


@dataclass(frozen=True)
class GetTwichUserByLogin(Query):
    login: str


@dataclass(frozen=True)
class GetAllTwichUsers(Query):
    pass
