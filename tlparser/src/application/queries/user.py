"""
user.py: File, containing twich user queries.
"""


from dataclasses import dataclass
from application.queries import Query


@dataclass(frozen=True)
class GetTwichUserByLogin(Query):
    login: str


@dataclass(frozen=True)
class GetAllTwichUsers(Query):
    pass
