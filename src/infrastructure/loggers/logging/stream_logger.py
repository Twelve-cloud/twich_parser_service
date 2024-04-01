"""
stream_logger.py: File, containing stream logger.
"""


from logging import INFO, Formatter, Logger, StreamHandler, getLogger
from shared.interfaces import ILogger


class StreamLogger(ILogger):
    def __init__(self, name: str = 'StreamLogger') -> None:
        self._configure_logger(name)

    def _configure_logger(self, name: str) -> None:
        self._logger: Logger = getLogger(name)
        self._logger.setLevel(INFO)

        stream_handler: StreamHandler = StreamHandler()
        stream_handler.setLevel(INFO)

        format_string: str = '[%(asctime)s] [Logger: %(name)s] [%(levelname)s] > %(message)s'
        format_date: str = '%Y-%m-%d %H:%M:%S'
        formatter: Formatter = Formatter(format_string, format_date)

        stream_handler.setFormatter(formatter)
        self._logger.addHandler(stream_handler)

    def info(self, message: str) -> None:
        self._logger.info(message)

    def debug(self, message: str) -> None:
        self._logger.debug(message)

    def warning(self, message: str) -> None:
        self._logger.warning(message)

    def error(self, message: str) -> None:
        self._logger.error(message)

    def critical(self, message: str) -> None:
        self._logger.critical(message)
