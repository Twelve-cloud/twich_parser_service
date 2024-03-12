"""
user.py: File, containing twich user commands.
"""


from dataclasses import dataclass
from application.commands import BaseCommand


@dataclass(frozen=True)
class ParseTwichUserCommand(BaseCommand):
    login: str


@dataclass(frozen=True)
class DeleteTwichUserCommand(BaseCommand):
    login: str
