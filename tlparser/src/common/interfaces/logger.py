"""
logger.py: File, containing logger interface.
"""


from interface import Interface


class ILogger(Interface):
    def _configure_logger(self, name: str) -> None:
        raise NotImplementedError

    def info(self, message: str) -> None:
        raise NotImplementedError

    def debug(self, message: str) -> None:
        raise NotImplementedError

    def warning(self, message: str) -> None:
        raise NotImplementedError

    def error(self, message: str) -> None:
        raise NotImplementedError

    def critical(self, message: str) -> None:
        raise NotImplementedError
