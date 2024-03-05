"""
base.py: File, containing base domain exception.
"""


class BaseDomainException(Exception):
    """
    BaseDomainException: Class, that represents base domain exception for all domain exceptions.
    It contains common data and behaviour for every domain exception.

    Args:
        Exception: Base class for base domain exception.
    """

    def __init__(self, message: str) -> None:
        """
        __init__: Initialize base domain exception instance.

        Args:
            message (str): Short error message.
        """

        self._message: str = message

    @property
    def message(self) -> str:
        """
        message: Return short error message.

        Returns:
            str: Short error message.
        """

        return self._message
