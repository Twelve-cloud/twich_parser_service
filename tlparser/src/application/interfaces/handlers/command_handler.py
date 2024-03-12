"""
command_handler.py: File, containing command handler interface.
"""


from typing import Generic, TypeVar
from interface import Interface
from application.commands import Command
from application.dto import Failure, Success


C = TypeVar('C', bound=Command)


class ICommandHandler(Generic[C], Interface):
    async def handle(self, command: C) -> Success | Failure:
        raise NotImplementedError
