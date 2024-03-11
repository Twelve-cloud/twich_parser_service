"""
logger.py: File, containing logger interface.
"""


from interface import Interface


class ILogger(Interface):
    def _configure_logger(self, name: str) -> None:
        pass

    def info(self, message: str) -> None:
        pass

    def debug(self, message: str) -> None:
        pass

    def warning(self, message: str) -> None:
        pass

    def error(self, message: str) -> None:
        pass

    def critical(self, message: str) -> None:
        pass
