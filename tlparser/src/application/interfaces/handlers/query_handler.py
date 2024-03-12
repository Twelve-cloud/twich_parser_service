"""
query_handler.py: File, containing query handler interface.
"""


from typing import Generic, TypeVar
from interface import Interface
from application.dto import DTO
from application.queries import Query


Q = TypeVar('Q', bound=Query)
R = TypeVar('R', bound=DTO)


class IQueryHandler(Generic[Q, R], Interface):
    def handle(self, query: Q) -> R:
        raise NotImplementedError
