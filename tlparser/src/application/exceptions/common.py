"""
common.py: File, containing common application exceptions.
"""


from application.exceptions import BaseApplicationException


class TwichException(BaseApplicationException):
    """
    TwichException: Class that represents twich exception.

    Args:
        BaseApplicationException: Base application exception class.
    """

    def __init__(self, message: str) -> None:
        """
        __init__: Initialize twich exception.

        Args:
            message (str): Message why exception has been occured.
        """

        super().__init__(message)


class RequestTimeoutException(BaseApplicationException):
    """
    RequestTimeoutException: Class that represents request timeout exception.

    Args:
        BaseApplicationException: Base application exception class.
    """

    def __init__(self, message: str) -> None:
        """
        __init__: Initialize request timeout exception.

        Args:
            message (str): Message why exception has been occured.
        """

        super().__init__(message)


class NotFoundException(BaseApplicationException):
    """
    NotFoundException: Class that represents not found exception.

    Args:
        BaseApplicationException: Base application exception class.
    """

    def __init__(self, message: str) -> None:
        """
        __init__: Initialize not found exception.

        Args:
            message (str): Message why exception has been occured.
        """

        super().__init__(message)


class ServiceUnavailableException(BaseApplicationException):
    """
    ServiceUnavailableException: Class that represents service unavailable exception.

    Args:
        BaseApplicationException: Base application exception class.
    """

    def __init__(self, message: str) -> None:
        """
        __init__: Initialize service unavailable exception.

        Args:
            message (str): Message why exception has been occured.
        """

        super().__init__(message)
