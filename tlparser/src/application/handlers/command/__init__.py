"""
__init__.py: File, containing other command handler modules to simplify import.
"""


from application.handlers.command.game import (
    DeleteTwichGameByNameHandler,
    DeleteTwichGameHandler,
    ParseTwichGameHandler,
)
from application.handlers.command.stream import (
    DeleteTwichStreamByUserLoginHandler,
    DeleteTwichStreamHandler,
    ParseTwichStreamHandler,
)
from application.handlers.command.user import (
    DeleteTwichUserByLoginHandler,
    DeleteTwichUserHandler,
    ParseTwichUserHandler,
)


__all__: list[str] = [
    'DeleteTwichGameByNameHandler',
    'DeleteTwichGameHandler',
    'ParseTwichGameHandler',
    'DeleteTwichStreamByUserLoginHandler',
    'DeleteTwichStreamHandler',
    'ParseTwichStreamHandler',
    'DeleteTwichUserByLoginHandler',
    'DeleteTwichUserHandler',
    'ParseTwichUserHandler',
]
