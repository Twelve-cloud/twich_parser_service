"""
query_handler.py: File, containing query handler interface.
"""


from abc import ABC as Interface, abstractmethod
from typing import Generic, TypeVar
from application.dto import DTO
from application.queries import Query


Q = TypeVar('Q', bound=Query)
R = TypeVar('R', bound=DTO)


class IQueryHandler(Interface, Generic[Q, R]):
    @abstractmethod
    async def handle(self, query: Q) -> R:
        raise NotImplementedError
