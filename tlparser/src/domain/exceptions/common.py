"""
common.py: File, containing common domain exceptions.
"""


from domain.exceptions import BaseDomainException


class TwichTokenNotObtainedException(BaseDomainException):
    """
    TwichTokenNotObtainedException: Class, that represents Twich token exception.
    It means that getting access token from twich does not succeed.

    Args:
        BaseDomainException: Base domain exception class.
    """

    def __init__(self, message: str, detailed_messages: list[str]) -> None:
        """
        __init__: Initialize twich token not obtained exception.

        Args:
            message (str): Short error message.
            detailed_messages (list[str]): List of all detailed error messages.
        """

        super().__init__(message, detailed_messages)


class TwichRequestUnauthorizedException(BaseDomainException):
    """
    TwichRequestUnauthorizedException: Class, that represents Twich request unauthorized exception.
    It means that request to twich API (for parsing) is unauthorized.

    Args:
        BaseDomainException: Base domain exception class.
    """

    def __init__(self, message: str, detailed_messages: list[str]) -> None:
        """
        __init__: Initialize twich request unauthorized exception.

        Args:
            message (str): Short error message.
            detailed_messages (list[str]): List of all detailed error messages.
        """

        super().__init__(message, detailed_messages)


class TwichGetObjectBadRequestException(BaseDomainException):
    """
    TwichGetObjectBadRequestException: Class, that represents TwichAPI bad request exception.
    It means that request to Twich API (for parsing) fails because of input data.

    Args:
        BaseDomainException: Base domain exception class.
    """

    def __init__(self, message: str, detailed_messages: list[str]) -> None:
        """
        __init__: Initialize twich get object bad request exception.

        Args:
            message (str): Short error message.
            detailed_messages (list[str]): List of all detailed error messages.
        """

        super().__init__(message, detailed_messages)


class TwichRequestTimeoutException(BaseDomainException):
    """
    TwichRequestTimeoutException: Class, that represents Twich request timeout exception.
    It means that request to Twich API (for parsing) is out of time.

    Args:
        BaseDomainException: Base domain exception class.
    """

    def __init__(self, message: str, detailed_messages: list[str]) -> None:
        """
        __init__: Initialize twich request timeout exception.

        Args:
            message (str): Short error message.
            detailed_messages (list[str]): List of all detailed error messages.
        """

        super().__init__(message, detailed_messages)


class ObjectNotFoundException(BaseDomainException):
    """
    ObjectNotFoundException: Class, that represents object not found exception.
    It means that request to Twich API for parsing could not parse object because it does not exist.

    Args:
        BaseDomainException: Base domain exception class.
    """

    def __init__(self, message: str, detailed_messages: list[str]) -> None:
        """
        __init__: Initialize object not found exception.

        Args:
            message (str): Short error message.
            detailed_messages (list[str]): List of all detailed error messages.
        """

        super().__init__(message, detailed_messages)


class ParserException(BaseDomainException):
    """
    ParserException: Class, that represents parser exception.
    It means that parser produces error during parsing.

    Args:
        BaseDomainException: Base domain exception class.
    """

    def __init__(self, message: str, detailed_messages: list[str]) -> None:
        """
        __init__: Initialize parser exception.

        Args:
            message (str): Short error message.
            detailed_messages (list[str]): List of all detailed error messages.
        """

        super().__init__(message, detailed_messages)
