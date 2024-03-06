"""
game.py: File, containing request handler interface for a twich game.
"""


from application.dtos.requests import TwichGameRequest
from application.dtos.responses import TwichGameResponse
from application.interfaces.handlers.requests import IBaseRequestHandler


class ITwichGameRequestHandler(IBaseRequestHandler[TwichGameRequest, TwichGameResponse]):
    """
    ITwichGameRequestHandler: Class that represents request handler interface for a twich game.

    Args:
        IBaseRequestHandler: Base request handler interface instantiated with appropriate classes.
    """

    pass
