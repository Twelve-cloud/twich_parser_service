"""
base.py: File, containing base application exceptions.
"""


class BaseApplicationException(Exception):
    """
    BaseApplicationException: Class, that represents base application exception.
    It contains common data and behaviour for all application exceptions.

    Args:
        Exception: Base class for base application exception.
    """

    def __init__(self, message: str) -> None:
        """
        __init__: Initialize base application exception.

        Args:
            message (str): Message why exception has been occured.
        """

        self._message: str = message

    @property
    def message(self) -> str:
        """
        message: Return message why exception  has been occured.

        Returns:
            str: Message why exception has been occured.
        """

        return self._message
