"""
__init__.py: File, containing other query modules to simplify import.
"""


from application.queries.base import Query
from application.queries.game import (
    GetAllTwichGames,
    GetTwichGameByName,
)
from application.queries.stream import (
    GetAllTwichStreams,
    GetTwichStreamByUserLogin,
)
from application.queries.user import (
    GetAllTwichUsers,
    GetTwichUserByLogin,
)


__all__: list[str] = [
    'Query',
    'GetAllTwichGames',
    'GetTwichGameByName',
    'GetAllTwichStreams',
    'GetTwichStreamByUserLogin',
    'GetAllTwichUsers',
    'GetTwichUserByLogin',
]
