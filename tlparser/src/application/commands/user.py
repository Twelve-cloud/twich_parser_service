"""
user.py: File, containing twich user commands.
"""


from dataclasses import dataclass
from application.commands import Command


@dataclass(frozen=True)
class ParseTwichUserCommand(Command):
    login: str


@dataclass(frozen=True)
class DeleteTwichUserCommand(Command):
    login: str
