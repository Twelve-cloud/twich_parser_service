"""
game.py: File, containing twich game commands.
"""


from dataclasses import dataclass
from application.commands.base import Command


@dataclass(frozen=True)
class ParseTwichGame(Command):
    name: str


@dataclass(frozen=True)
class DeleteTwichGame(Command):
    id: int


@dataclass(frozen=True)
class DeleteTwichGameByName(Command):
    name: str
