"""
stream_logger.py: File, containing stream logger.
"""


from logging import Formatter, Logger, StreamHandler, getLogger, INFO
from common.interfaces import ILogger


class StreamLogger(ILogger):
    """
    StreamLogger: Class, that represents stream logger.

    Args:
        ILogger: Logger interface.
    """

    def __init__(self, name: str = 'StreamLogger') -> None:
        """
        __init__: Initialize stream logger.

        Args:
            name (str): Name of the logger.
        """

        self._configure_logger(name)

    def _configure_logger(self, name: str) -> None:
        """
        _configure_logger: Configure logger.
        It configure logger to write messages to output stream using special string format.

        Args:
            name (str): Name of the logger.
        """

        self._logger: Logger = getLogger(name)
        self._logger.setLevel(INFO)

        stream_handler: StreamHandler = StreamHandler()
        stream_handler.setLevel(INFO)

        format_string: str = '[%(asctime)s] [Logger: %(name)s] [%(levelname)s] > %(message)s'
        format_date: str = '%Y-%m-%d %H:%M:%S'
        formatter: Formatter = Formatter(format_string, format_date)

        stream_handler.setFormatter(formatter)
        self._logger.addHandler(stream_handler)

    def log(self, level: int, message: str) -> None:
        """
        log: Log message.

        Args:
            level (str): Message level.
            message (str): Message.
        """

        self._logger.log(level, message)
