"""
game.py: File, containing twich game commands.
"""


from dataclasses import dataclass
from application.commands import Command


@dataclass(frozen=True)
class ParseTwichGameCommand(Command):
    name: str


@dataclass(frozen=True)
class DeleteTwichGameCommand(Command):
    name: str
