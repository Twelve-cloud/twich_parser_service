"""
__init__.py: File, containing other query handler modules to simplify import.
"""


from application.handlers.query.decorators import (
    ExceptionHandlingDecorator,
    QueryHandlerDecorator,
)
from application.handlers.query.game import (
    GetAllTwichGamesHandler,
    GetTwichGameByNameHandler,
    GetTwichGameHandler,
)
from application.handlers.query.stream import (
    GetAllTwichStreamsHandler,
    GetTwichStreamByUserLoginHandler,
    GetTwichStreamHandler,
)
from application.handlers.query.user import (
    GetAllTwichUsersHandler,
    GetTwichUserByLoginHandler,
    GetTwichUserHandler,
)


__all__: list[str] = [
    'ExceptionHandlingDecorator',
    'QueryHandlerDecorator',
    'GetAllTwichGamesHandler',
    'GetTwichGameByNameHandler',
    'GetTwichGameHandler',
    'GetAllTwichStreamsHandler',
    'GetTwichStreamByUserLoginHandler',
    'GetTwichStreamHandler',
    'GetAllTwichUsersHandler',
    'GetTwichUserByLoginHandler',
    'GetTwichUserHandler',
]
