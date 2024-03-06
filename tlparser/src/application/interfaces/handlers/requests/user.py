"""
user.py: File, containing request handler interface for a twich user.
"""


from application.dtos.requests import TwichUserRequest
from application.dtos.responses import TwichUserResponse
from application.interfaces.handlers.requests import IBaseRequestHandler


class ITwichUserRequestHandler(IBaseRequestHandler[TwichUserRequest, TwichUserResponse]):
    """
    ITwichUserRequestHandler: Class that represents request handler interface for a twich user.

    Args:
        IBaseRequestHandler: Base request handler interface instantiated with appropriate classes.
    """

    pass
