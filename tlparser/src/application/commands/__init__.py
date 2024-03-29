"""
__init__.py: File, containing other command modules to simplify import.
"""


from typing import TypeVar
from application.commands.base import Command
from application.commands.game import (
    DeleteTwichGame,
    DeleteTwichGameByName,
    ParseTwichGame,
)
from application.commands.stream import (
    DeleteTwichStream,
    DeleteTwichStreamByUserLogin,
    ParseTwichStream,
)
from application.commands.user import (
    DeleteTwichUser,
    DeleteTwichUserByLogin,
    ParseTwichUser,
)


C = TypeVar('C', bound=Command)


__all__: list[str] = [
    'Command',
    'DeleteTwichGame',
    'DeleteTwichGameByName',
    'ParseTwichGame',
    'DeleteTwichStream',
    'DeleteTwichStreamByUserLogin',
    'ParseTwichStream',
    'DeleteTwichUser',
    'DeleteTwichUserByLogin',
    'ParseTwichUser',
    'C',
]
