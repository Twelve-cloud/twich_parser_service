"""
twich_exceptions.py: File, containing exceptions for a twich app.
"""


class GetGameBadRequestException(Exception):
    """
    GetGameBadRequestException: Class, that represents TwichAPI bad request to get game.

    Args:
        Exception (_type_): Base superclass for GetGameBadRequestException.
    """

    reasons: list[str] = [
        'The request must specify the id or name or igdb_id query parameter.',
        'The combined number of game IDs and game names in the request must not exceed 100.',
    ]


class GetGameUnauthorizedException(Exception):
    """
    GetGameUnauthorizedException: Class, that represents TwichAPI unauthorized to get game.

    Args:
        Exception (_type_): Base superclass for GetGameUnauthorizedException.
    """

    reasons: list[str] = [
        'The Authorization header is required',
        'The access token is not valid.',
        'The ID in the Client-Id header must match the client ID in the access token.',
    ]


class GameNotFoundException(Exception):
    """
    GameNotFoundException: Class, that represents that game is not found.

    Args:
        Exception (_type_): Base superclass for GameNotFoundException
    """

    reasons: list[str] = [
        'The ID of the game is wrong.',
    ]


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


class GetStreamBadRequestException(Exception):
    """
    GetStreamBadRequestException: Class, that represents TwichAPI bad request to get stream.

    Args:
        Exception (_type_): Base superclass for GetStreamBadRequestException.
    """

    reasons: list[str] = [
        'The value in the type query parameter is not valid.',
    ]


class GetStreamUnauthorizedException(Exception):
    """
    GetStreamUnauthorizedException: Class, that represents TwichAPI unauthorized to get stream.

    Args:
        Exception (_type_): Base superclass for GetStreamUnauthorizedException.
    """

    reasons: list[str] = [
        'The Authorization header is required',
        'The access token is not valid.',
        'The ID in the Client-Id header must match the client ID in the access token.',
    ]


class StreamNotFoundException(Exception):
    """
    StreamNotFoundException: Class, that represents that stream is not found.

    Args:
        Exception (_type_): Base superclass for StreamNotFoundException
    """

    reasons: list[str] = [
        'The ID of the stream is wrong.',
    ]
