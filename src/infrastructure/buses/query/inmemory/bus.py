"""
bus.py: File, containing in memory query bus implementation.
"""


from application.interfaces.bus import IQueryBus
from application.interfaces.handler import IQueryHandler
from application.queries import Query
from application.dto import RD


class InMemoryQueryBus(IQueryBus):
    def __init__(self) -> None:
        self.handlers: dict[type[Query], IQueryHandler] = {}

    def register(self, query_class: type[Query], query_handler: IQueryHandler) -> None:
        self.handlers[query_class] = query_handler

    async def dispatch(self, query: Query) -> RD:
        handler: IQueryHandler = self.handlers[type(query)]

        return await handler.handle(query)
