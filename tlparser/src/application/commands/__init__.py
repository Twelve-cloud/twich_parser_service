"""
__init__.py: File, containing other command modules to simplify import.
"""


from typing import TypeVar
from application.commands.base import Command
from application.commands.game import (
    DeleteTwichGame,
    ParseTwichGame,
)
from application.commands.stream import (
    DeleteTwichStream,
    ParseTwichStream,
)
from application.commands.user import (
    DeleteTwichUser,
    ParseTwichUser,
)


C = TypeVar('C', bound=Command)


__all__: list[str] = [
    'Command',
    'DeleteTwichGame',
    'ParseTwichGame',
    'DeleteTwichStream',
    'ParseTwichStream',
    'DeleteTwichUser',
    'ParseTwichUser',
    'C',
]
