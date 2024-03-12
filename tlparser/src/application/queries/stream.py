"""
game.py: File, containing twich stream queries.
"""


from dataclasses import dataclass
from application.queries import BaseQuery


@dataclass(frozen=True)
class GetTwichStreamByUserLoginQuery(BaseQuery):
    user_login: str


@dataclass(frozen=True)
class GetAllTwichStreamsQuery(BaseQuery):
    pass
