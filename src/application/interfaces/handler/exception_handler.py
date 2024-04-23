"""
exception_handler.py: File, containing exception handler interface.
"""


from abc import (
    ABC as Interface,
    abstractmethod,
)
from typing import (
    Any,
    Generic,
)

from application.exceptions import E


class IExceptionHandler(Interface, Generic[E]):
    @abstractmethod
    async def handle(self, exception: E) -> Any:
        raise NotImplementedError
