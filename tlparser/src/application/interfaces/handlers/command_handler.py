"""
command_handler.py: File, containing command handler interface.
"""


from abc import ABC as Interface, abstractmethod
from typing import Generic, TypeVar
from application.commands import Command
from application.dto import Failure, Success


C = TypeVar('C', bound=Command)


class ICommandHandler(Interface, Generic[C]):
    @abstractmethod
    async def handle(self, command: C) -> Success | Failure:
        raise NotImplementedError
