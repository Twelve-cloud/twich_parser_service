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

    def __init__(self, message: str, detailed_messages: list[str]) -> None:
        """
        __init__: Initialize base domain exception instance.

        Args:
            message (str): Short error message.
            detailed_messages (list[str]): List of all detailed error messages.
        """

        self._message: str = message
        self._detailed_messages: list[str] = detailed_messages

    @property
    def message(self) -> str:
        """
        message: Return short error message.

        Returns:
            str: Short error message.
        """

        return self._message

    @property
    def detailed_messages(self) -> list[str]:
        """
        detailed_messages: Return list of all detailed error messages.

        Returns:
            list[str]: List of all detailed error messages.
        """

        return self._detailed_messages
