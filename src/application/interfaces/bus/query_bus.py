"""
base.py: File, containing query bus interface.
"""


from abc import ABC as Interface
from abc import abstractmethod

from application.dto import RD
from application.interfaces.handler import IQueryHandler
from application.queries import Query


class IQueryBus(Interface):
    @abstractmethod
    def register(self, query_class: type[Query], query_handler: IQueryHandler) -> None:
        raise NotImplementedError

    @abstractmethod
    async def dispatch(self, query: Query) -> RD:
        raise NotImplementedError
