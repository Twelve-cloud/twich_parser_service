"""
decorator.py: File, containing decorator interface.
"""


from abc import ABCMeta, abstractmethod
from typing import Any


class IDecorator(metaclass=ABCMeta):
    """
    IDecorator: Class, that represents decorator interface.

    Args:
        ABCMeta: Base metaclass for decorator interface that make this class abstract.
    """

    @abstractmethod
    def __getattr__(self, name: str) -> Any:
        """
        __getattr__: Should translate all calls to decorated object.
        Must be overriden.

        Args:
            name (str): Name of the attribute.

        Returns:
            Any: Any value that decorated object returns.
        """

        pass
