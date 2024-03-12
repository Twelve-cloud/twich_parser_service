"""
stream.py: File, containing twich stream commands.
"""


from dataclasses import dataclass
from application.commands import BaseCommand


@dataclass(frozen=True)
class ParseTwichStreamCommand(BaseCommand):
    user_login: str


@dataclass(frozen=True)
class DeleteTwichStreamCommand(BaseCommand):
    user_login: str
