"""
base.py: File, containing base request handler interface.
"""


from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar
from application.dtos.requests import BaseRequest
from application.dtos.responses import BaseResponse


RQ = TypeVar('RQ', bound=BaseRequest)
RS = TypeVar('RS', bound=BaseResponse)


class IBaseRequestHandler(Generic[RQ, RS], metaclass=ABCMeta):
    """
    IBaseRequestHandler: Class, that represents base request handler interface.
    It contains common methods for every request handler.

    Args:
        Generic: Base class for base request handler interface that make this class template.
        ABCMeta: Base metaclass for base request handler interface that make this class abstract.
    """

    @abstractmethod
    def handle(self, request: RQ) -> RS:
        """
        handle: Handle request.

        Args:
            request (RQ): Request.

        Returns:
            RS: Response.
        """

        pass
