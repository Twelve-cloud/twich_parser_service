"""
query_bus.py: File, containing command bus interface.
"""


from abc import ABC as Interface
from abc import abstractmethod
from typing import Generic, TypeVar
from application.dto import DTO
from application.interfaces.handlers import IQueryHandler
from application.queries import Query


Q = TypeVar('Q', bound=Query)
H = TypeVar('H', bound=IQueryHandler)
R = TypeVar('R', bound=DTO)


class IQueryBus(Interface, Generic[Q, H, R]):
    @abstractmethod
    def register(self, query_class: type[Q], query_handler: H) -> None:
        raise NotImplementedError

    @abstractmethod
    def execute(self, query: Q) -> R:
        raise NotImplementedError
