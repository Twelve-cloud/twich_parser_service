"""
command_handler.py: File, containing command handler interface.
"""


from abc import ABC as Interface
from abc import abstractmethod
from typing import Generic

from application.commands import C
from application.dto import ResultDTO


class ICommandHandler(Interface, Generic[C]):
    @abstractmethod
    async def handle(self, command: C) -> ResultDTO:
        raise NotImplementedError
