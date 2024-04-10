"""
exception_handler.py: File, containing exception handler interface.
"""


from abc import ABC as Interface
from abc import abstractmethod
from typing import (
    Any,
    Generic,
    TypeVar,
)


E = TypeVar('E', bound=Exception)


class IExceptionHandler(Interface, Generic[E]):
    @abstractmethod
    def handle(self, exception: E) -> Any:
        pass
