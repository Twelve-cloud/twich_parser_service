"""
stream.py: File, containing request handler interface for a twich stream.
"""


from application.dtos.requests import TwichStreamRequest
from application.dtos.responses import TwichStreamResponse
from application.interfaces.handlers.requests import IBaseRequestHandler


class ITwichStreamRequestHandler(IBaseRequestHandler[TwichStreamRequest, TwichStreamResponse]):
    """
    ITwichStreamRequestHandler: Class that represents request handler interface for a twich stream.

    Args:
        IBaseRequestHandler: Base request handler interface instantiated with appropriate classes.
    """

    pass
