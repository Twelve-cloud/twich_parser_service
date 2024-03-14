"""
user.py: File, containing twich user commands.
"""


from dataclasses import dataclass
from application.commands.base import Command


@dataclass(frozen=True)
class ParseTwichUser(Command):
    """
    ParseTwichUser: Class, representing parse twich user command.

    Bases:
        1) Command: Base command class. Every command should be inherited from this class.
    """

    login: str


@dataclass(frozen=True)
class DeleteTwichUser(Command):
    """
    DeleteTwichUser: Class, representing delete twich user command.

    Bases:
        1) Command: Base command class. Every command should be inherited from this class.
    """

    login: str
