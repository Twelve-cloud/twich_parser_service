"""
game.py: File, containing twich game commands.
"""


from dataclasses import dataclass
from application.commands.base import Command


@dataclass(frozen=True)
class ParseTwichGame(Command):
    """
    ParseTwichGame: Class, representing parse twich game command.

    Bases:
        1) Command: Base command class. Every command should be inherited from this class.
    """

    name: str


@dataclass(frozen=True)
class DeleteTwichGame(Command):
    """
    DeleteTwichGame: Class, representing delete twich game command.

    Bases:
        1) Command: Base command class. Every command should be inherited from this class.
    """

    name: str
