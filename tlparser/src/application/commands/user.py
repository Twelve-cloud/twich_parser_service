"""
user.py: File, containing twich user commands.
"""


from dataclasses import dataclass
from application.commands.base import Command


@dataclass(frozen=True)
class ParseTwichUser(Command):
    login: str


@dataclass(frozen=True)
class DeleteTwichUser(Command):
    login: str
