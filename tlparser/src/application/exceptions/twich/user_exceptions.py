"""
user_exceptions.py: File, containing exceptions for a twich user.
"""


class GetUserBadRequestException(Exception):
    """
    GetUserBadRequestException: Class, that represents TwichAPI bad request to get user.

    Args:
        Exception (_type_): Base superclass for GetUserBadRequestException.
    """

    reasons: list[str] = [
        'The id or login query parameter is required unless the request uses a user access token.',
        'The request exceeded the maximum allowed number of id and/or login query parameters.',
    ]


class GetUserUnauthorizedException(Exception):
    """
    GetUserUnauthorizedException: Class, that represents TwichAPI unauthorized to get user.

    Args:
        Exception (_type_): Base superclass for GetUserUnauthorizedException.
    """

    reasons: list[str] = [
        'The Authorization header is required',
        'The access token is not valid.',
        'The ID in the Client-Id header must match the client ID in the access token.',
    ]


class UserNotFoundException(Exception):
    """
    UserNotFoundException: Class, that represents that user is not found.

    Args:
        Exception (_type_): Base superclass for UserNotFoundException
    """

    reasons: list[str] = [
        'The ID of the user is wrong.',
    ]
