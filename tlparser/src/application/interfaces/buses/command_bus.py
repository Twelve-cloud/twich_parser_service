"""
command_bus.py: File, containing command bus interface.
"""


from abc import ABC as Interface
from abc import abstractmethod
from typing import Generic, TypeVar
from application.commands import Command
from application.dto import Result
from application.interfaces.handlers import ICommandHandler


C = TypeVar('C', bound=Command)
H = TypeVar('H', bound=ICommandHandler)


class ICommandBus(Interface, Generic[C, H]):
    @abstractmethod
    def register(self, command_class: type[C], command_handler: H) -> None:
        raise NotImplementedError

    @abstractmethod
    def execute(self, command: C) -> Result:
        raise NotImplementedError
