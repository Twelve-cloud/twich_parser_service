"""
bus.py: File, containing in memory query bus implementation.
"""


from application.dto import RD
from application.interfaces.bus import IQueryBus
from application.interfaces.handler import IQueryHandler
from application.queries import Query


class InMemoryQueryBus(IQueryBus):
    def __init__(self, query_handlers: dict[type[Query], IQueryHandler]) -> None:
        self._query_handlers: dict[type[Query], IQueryHandler] = query_handlers

    def register(self, query_class: type[Query], query_handler: IQueryHandler) -> None:
        self._query_handlers[query_class] = query_handler

    async def dispatch(self, query: Query) -> RD:
        handler: IQueryHandler = self._query_handlers[type(query)]

        return await handler.handle(query)
