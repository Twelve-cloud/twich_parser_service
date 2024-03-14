"""
logger.py: File, containing logger interface.
"""


from abc import ABC as Interface
from abc import abstractmethod


class ILogger(Interface):
    """
    ILogger: Class, representing logger interface. This class is an interface.
    You can create an instance of this class, but Interface shows that you should not do this.
    Interface base class is Abstract Base Class. It is called Interface to make intention explicit.

    Bases:
        1) Interface: Abstract Base Class. It is a marker this class provide interface only.
    """

    @abstractmethod
    def _configure_logger(self, name: str) -> None:
        """
        _configure_logger: Shold configure logger.
        Must be overriden.

        Args:
            name (str): Name of the logger.

        Raises:
            NotImplementedError: Raises to prevent calling this method by super.
        """

        raise NotImplementedError

    @abstractmethod
    def info(self, message: str) -> None:
        """
        info: Should write info message.
        Must be overriden.

        Args:
            message (str): Info message.

        Raises:
            NotImplementedError: Raises to prevent calling this method by super.
        """

        raise NotImplementedError

    @abstractmethod
    def debug(self, message: str) -> None:
        """
        debug: Should write debug message.
        Must be overriden.

        Args:
            message (str): Debug message.

        Raises:
            NotImplementedError: Raises to prevent calling this method by super.
        """

        raise NotImplementedError

    @abstractmethod
    def warning(self, message: str) -> None:
        """
        warning: Should write warning message.
        Must be overriden.

        Args:
            message (str): Warning message.

        Raises:
            NotImplementedError: Raises to prevent calling this method by super.
        """

        raise NotImplementedError

    @abstractmethod
    def error(self, message: str) -> None:
        """
        error: Should write error message.
        Must be overriden.

        Args:
            message (str): Error message.

        Raises:
            NotImplementedError: Raises to prevent calling this method by super.
        """

        raise NotImplementedError

    @abstractmethod
    def critical(self, message: str) -> None:
        """
        critical: Should write critical message.
        Must be overriden.

        Args:
            message (str): Critical message.

        Raises:
            NotImplementedError: Raises to prevent calling this method by super.
        """

        raise NotImplementedError
