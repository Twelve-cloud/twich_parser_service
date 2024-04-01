"""
base.py: File, containing command bus interface.
"""


from abc import ABC as Interface
from abc import abstractmethod

from application.commands import Command
from application.dto import ResultDTO
from application.interfaces.handler import ICommandHandler


class ICommandBus(Interface):
    @abstractmethod
    def register(self, command_class: type[Command], command_handler: ICommandHandler) -> None:
        raise NotImplementedError

    @abstractmethod
    async def dispatch(self, command: Command) -> ResultDTO:
        raise NotImplementedError
