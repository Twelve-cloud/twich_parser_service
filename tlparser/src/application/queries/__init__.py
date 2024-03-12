"""
__init__.py: File, containing other query modules to simplify import.
"""


from application.queries.base import Query
from application.queries.game import (
    GetAllTwichGamesQuery,
    GetTwichGameByNameQuery,
)
from application.queries.stream import (
    GetAllTwichStreamsQuery,
    GetTwichStreamByUserLoginQuery,
)
from application.queries.user import (
    GetAllTwichUsersQuery,
    GetTwichUserByLoginQuery,
)


__all__: list[str] = [
    'Query',
    'GetAllTwichGamesQuery',
    'GetTwichGameByNameQuery',
    'GetAllTwichStreamsQuery',
    'GetTwichStreamByUserLoginQuery',
    'GetAllTwichUsersQuery',
    'GetTwichUserByLoginQuery',
]
