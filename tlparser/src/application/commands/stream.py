"""
stream.py: File, containing twich stream commands.
"""


from dataclasses import dataclass
from application.commands import Command


@dataclass(frozen=True)
class ParseTwichStreamCommand(Command):
    user_login: str


@dataclass(frozen=True)
class DeleteTwichStreamCommand(Command):
    user_login: str
