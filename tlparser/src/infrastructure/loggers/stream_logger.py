"""
stream_logger.py: File, containing stream logger.
"""


import logging
from logging import Formatter, Logger, StreamHandler, getLogger
from typing import Any
from common.interfaces.loggers import ILogger


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

        self.logger: Logger = self._configure_and_get_logger(name)

    def _configure_and_get_logger(self, name: str) -> Logger:
        """
        _configure_and_get_logger: Configure and return logger.
        It configure logger to write messages to output stream using special string format.

        Args:
            name (str): Name of the logger.

        Returns:
            Logger: Configured logger instance.
        """

        logger: Logger = getLogger(name)
        logger.setLevel(logging.INFO)

        stream_handler: StreamHandler = StreamHandler()
        stream_handler.setLevel(logging.INFO)

        format_string: str = (
            '[%(asctime)s] [Filename: %(filename)s] [Lineno: %(lineno)s] '
            '[Logger: %(name)s] [%(levelname)s] > %(message)s'
        )
        format_date: str = '%Y-%m-%d %H:%M:%S'
        formatter: Formatter = Formatter(format_string, format_date)

        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        return logger

    def __getattr__(self, name: str) -> Any:
        """
        __getattr__: Translate all calls to self.logger.

        Args:
            name (str): Name of the attribute.

        Returns:
            Any: Any value that self.logger returns.
        """

        return getattr(self.logger, name)
