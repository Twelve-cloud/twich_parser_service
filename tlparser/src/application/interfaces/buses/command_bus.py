"""
base.py: File, containing command bus interface.
"""


from abc import ABC as Interface
from abc import abstractmethod
from typing import Generic
from application.commands import C
from application.dto import Result
from application.interfaces.handlers import CH


class ICommandBus(Interface, Generic[C, CH]):
    """
    ICommandBus: Class, representing command bus interface. This class is an interface.
    You can create an instance of this class, but Interface shows that you should not do this.
    Interface base class is Abstract Base Class. It is called Interface to make intention explicit.

    Bases:
        1) Interface: Abstract Base Class. It is a marker that this class provides interface only.
        2) Generic[C, CH]: Generic class. This class makes command bus interface generic.
    """

    @abstractmethod
    def register(self, command_class: type[C], command_handler: CH) -> None:
        """
        register: Should register command in command bus.
        Must be overriden.

        Args:
            command_class (type[C]): Class of the command.
            command_handler (CH): Command handler.

        Raises:
            NotImplementedError: Raises to prevent calling this method by super.
        """

        raise NotImplementedError

    @abstractmethod
    def dispatch(self, command: C) -> Result:
        """
        dispatch: Should dispatch command to command handler.
        Must be overriden.

        Args:
            command (C): Command.

        Raises:
            NotImplementedError: Raises to prevent calling this method by super.

        Returns:
            Result: Any result that command handler returns.
        """

        raise NotImplementedError
