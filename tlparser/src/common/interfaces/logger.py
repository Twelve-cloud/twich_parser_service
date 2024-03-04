"""
logger.py: File, containing logger interface.
"""


from abc import ABCMeta, abstractmethod
from logging import Logger
from typing import Any


class ILogger(metaclass=ABCMeta):
    """
    ILogger: Class, that represents logger interface.

    Args:
        ABCMeta: Base metaclass for logger interface that make this class abstract.
    """

    @abstractmethod
    def _configure_and_get_logger(self, name: str) -> Logger:
        """
        _configure_and_get_logger: Should configure up and return logger.
        Must be overriden.

        Args:
            name (str): Name of the logger.

        Returns:
            Logger: Configured logger instance.
        """

        pass

    @abstractmethod
    def __getattr__(self, name: str) -> Any:
        """
        __getattr__: Should translate all calls to logging.logger.
        Must be overriden.

        Args:
            name (str): Name of the attribute.

        Returns:
            Any: Any value that logging.logger returns.
        """

        pass
