"""
game.py: File, containing twich stream queries.
"""


from dataclasses import dataclass

from application.queries.base import Query


@dataclass(frozen=True)
class GetTwichStream(Query):
    id: int


@dataclass(frozen=True)
class GetTwichStreamByUserLogin(Query):
    user_login: str


@dataclass(frozen=True)
class GetAllTwichStreams(Query):
    pass
