"""
__init__.py: File, containing other query modules to simplify import.
"""


from typing import TypeVar

from application.queries.base import Query
from application.queries.game import (
    GetAllTwichGames,
    GetTwichGame,
    GetTwichGameByName,
)
from application.queries.stream import (
    GetAllTwichStreams,
    GetTwichStream,
    GetTwichStreamByUserLogin,
)
from application.queries.user import (
    GetAllTwichUsers,
    GetTwichUser,
    GetTwichUserByLogin,
)


Q = TypeVar('Q', bound=Query)


__all__: list[str] = [
    'Query',
    'GetAllTwichGames',
    'GetTwichGame',
    'GetTwichGameByName',
    'GetAllTwichStreams',
    'GetTwichStream',
    'GetTwichStreamByUserLogin',
    'GetAllTwichUsers',
    'GetTwichUser',
    'GetTwichUserByLogin',
    'Q',
]
