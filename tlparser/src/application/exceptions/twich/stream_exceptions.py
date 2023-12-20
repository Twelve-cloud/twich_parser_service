"""
stream_exceptions.py: File, containing exceptions for a twich stream.
"""


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
