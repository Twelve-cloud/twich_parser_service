"""
bus.py: File, containing in memory query bus implementation.
"""


from application.interfaces.buses import IQueryBus
from application.interfaces.handlers import IQueryHandler
from application.queries import Query
from application.dto import DTO


class InMemoryQueryBus(IQueryBus):
    def __init__(self) -> None:
        self.handlers: dict[type[Query], IQueryHandler] = {}

    def register(self, query_class: type[Query], query_handler: IQueryHandler) -> None:
        self.handlers[query_class] = query_handler

    async def dispatch(self, query: Query) -> DTO:
        handler: IQueryHandler = self.handlers[type(query)]

        return await handler.handle(query)
