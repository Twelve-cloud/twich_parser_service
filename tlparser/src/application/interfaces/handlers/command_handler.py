"""
command_handler.py: File, containing command handler interface.
"""


from typing import Generic, TypeVar
from interface import Interface
from application.commands import Command
from application.dto import FailureDTO, SuccessDTO


C = TypeVar('C', bound=Command)


class ICommandHandler(Generic[C], Interface):
    def handle(self, command: C) -> SuccessDTO | FailureDTO:
        raise NotImplementedError
