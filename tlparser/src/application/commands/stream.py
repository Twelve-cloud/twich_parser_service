"""
stream.py: File, containing twich stream commands.
"""


from dataclasses import dataclass
from application.commands.base import Command


@dataclass(frozen=True)
class ParseTwichStream(Command):
    """
    ParseTwichStream: Class, representing parse twich stream command.

    Bases:
        1) Command: Base command class. Every command should be inherited from this class.
    """

    user_login: str


@dataclass(frozen=True)
class DeleteTwichStream(Command):
    """
    DeleteTwichStream: Class, representing delete twich stream command.

    Bases:
        1) Command: Base command class. Every command should be inherited from this class.
    """

    user_login: str
