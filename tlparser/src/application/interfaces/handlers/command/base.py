"""
base.py: File, containing command handler interface.
"""


from abc import ABC as Interface
from abc import abstractmethod
from typing import Generic, TypeVar
from application.commands import Command
from application.dto import Result


C = TypeVar('C', bound=Command)


class ICommandHandler(Interface, Generic[C]):
    @abstractmethod
    async def handle(self, command: C) -> Result:
        raise NotImplementedError
