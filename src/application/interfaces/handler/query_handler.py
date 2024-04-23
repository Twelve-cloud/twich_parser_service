"""
query_handler.py: File, containing query handler interface.
"""


from abc import (
    ABC as Interface,
    abstractmethod,
)
from typing import Generic

from application.dto import RD
from application.queries import Q


class IQueryHandler(Interface, Generic[Q, RD]):
    @abstractmethod
    async def handle(self, query: Q) -> RD:
        raise NotImplementedError
