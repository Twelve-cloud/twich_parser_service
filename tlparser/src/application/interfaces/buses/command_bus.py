"""
base.py: File, containing command bus interface.
"""


from abc import ABC as Interface
from abc import abstractmethod
from application.commands import Command
from application.interfaces.handlers import ICommandHandler
from application.dto import Result


class ICommandBus(Interface):
    @abstractmethod
    def register(self, command_class: type[Command], command_handler: ICommandHandler) -> None:
        raise NotImplementedError

    @abstractmethod
    async def dispatch(self, command: Command) -> Result:
        raise NotImplementedError
