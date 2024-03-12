"""
__init__.py: File, containing other query handler modules to simplify import.
"""


from application.handlers.queries.game import (
    GetAllTwichGamesHandler,
    GetTwichGameByNameHandler,
)
from application.handlers.queries.stream import (
    GetAllTwichStreamsHandler,
    GetTwichStreamByUserLoginHandler,
)
from application.handlers.queries.user import (
    GetAllTwichUsersHandler,
    GetTwichUserByLoginHandler,
)


__all__: list[str] = [
    'GetAllTwichGamesHandler',
    'GetTwichGameByNameHandler',
    'GetAllTwichStreamsHandler',
    'GetTwichStreamByUserLoginHandler',
    'GetAllTwichUsersHandler',
    'GetTwichUserByLoginHandler',
]
