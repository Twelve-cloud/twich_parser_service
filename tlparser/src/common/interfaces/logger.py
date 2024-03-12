"""
logger.py: File, containing logger interface.
"""


from abc import ABC as Interface, abstractmethod


class ILogger(Interface):
    @abstractmethod
    def _configure_logger(self, name: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def info(self, message: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def debug(self, message: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def warning(self, message: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def error(self, message: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def critical(self, message: str) -> None:
        raise NotImplementedError
