"""
command_handler.py: File, containing command handler interface.
"""


from abc import ABC as Interface
from abc import abstractmethod
from typing import Generic
from application.commands import C
from application.dto import Result


class ICommandHandler(Interface, Generic[C]):
    """
    ICommandHandler: Class, representing command handler interface. This class is an interface.
    You can create an instance of this class, but Interface shows that you should not do this.
    Interface base class is Abstract Base Class. It is called Interface to make intention explicit.

    Bases:
        1) Interface: Abstract Base Class. It is a marker that this class provides interface only.
        2) Generic[C]: Generic class. This class makes repository interface generic.
    """

    @abstractmethod
    async def handle(self, command: C) -> Result:
        """
        handle: Should handle command.
        Must be overriden.

        Args:
            command (C): Command instance.

        Raises:
            NotImplementedError: Raises to prevent calling this method by super.

        Returns:
            Result: Result of the command.
        """

        raise NotImplementedError
