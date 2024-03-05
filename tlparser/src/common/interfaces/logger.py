"""
logger.py: File, containing logger interface.
"""


from abc import ABCMeta, abstractmethod
from typing import ClassVar


class ILogger(metaclass=ABCMeta):
    """
    ILogger: Class, that represents logger interface.

    Args:
        ABCMeta: Base metaclass for logger interface that make this class abstract.
    """

    DEBUG: ClassVar[int] = 10
    INFO: ClassVar[int] = 20
    WARNING: ClassVar[int] = 30
    ERROR: ClassVar[int] = 40
    CRITICAL: ClassVar[int] = 50

    @abstractmethod
    def _configure_logger(self, name: str) -> None:
        """
        _configure_logger: Should configure logger.
        Must be overriden.

        Args:
            name (str): Name of the logger.
        """

        pass

    @abstractmethod
    def log(self, level: int, message: str) -> None:
        """
        log: Should log message.
        Must be overriden.

        Args:
            level (str): Message level.
            message (str): Message.
        """

        pass
