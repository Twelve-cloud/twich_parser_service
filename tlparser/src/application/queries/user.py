"""
user.py: File, containing twich user queries.
"""


from dataclasses import dataclass
from application.queries import BaseQuery


@dataclass(frozen=True)
class GetTwichUserByLoginQuery(BaseQuery):
    login: str


@dataclass(frozen=True)
class GetAllTwichUsersQuery(BaseQuery):
    pass
