"""
__init__.py: File, containing other command modules to simplify import.
"""


from application.commands.base import Command
from application.commands.common import C
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


__all__: list[str] = [
    'Command',
    'C',
    'DeleteTwichGame',
    'ParseTwichGame',
    'DeleteTwichStream',
    'ParseTwichStream',
    'DeleteTwichUser',
    'ParseTwichUser',
]
