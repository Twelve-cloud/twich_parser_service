"""
game.py: File, containing twich game commands.
"""


from dataclasses import dataclass
from application.commands import BaseCommand


@dataclass(frozen=True)
class ParseTwichGameCommand(BaseCommand):
    name: str


@dataclass(frozen=True)
class DeleteTwichGameCommand(BaseCommand):
    name: str
