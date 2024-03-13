"""
__init__.py: File, containing other query handler modules to simplify import.
"""


from application.handlers.query.game import (
    GetAllTwichGamesHandler,
    GetTwichGameByNameHandler,
)
from application.handlers.query.stream import (
    GetAllTwichStreamsHandler,
    GetTwichStreamByUserLoginHandler,
)
from application.handlers.query.user import (
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
