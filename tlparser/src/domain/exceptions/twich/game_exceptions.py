"""
game_exceptions.py: File, containing exceptions for a twich game.
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
