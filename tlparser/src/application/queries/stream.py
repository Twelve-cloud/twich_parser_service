"""
game.py: File, containing twich stream queries.
"""


from dataclasses import dataclass
from application.queries import Query


@dataclass(frozen=True)
class GetTwichStreamByUserLoginQuery(Query):
    user_login: str


@dataclass(frozen=True)
class GetAllTwichStreamsQuery(Query):
    pass
