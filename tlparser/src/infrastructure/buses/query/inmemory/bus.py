"""
bus.py: File, containing in memory query bus implementation.
"""


from application.interfaces.buses import IQueryBus
from application.interfaces.handlers import QH
from application.queries import Q
from application.dto import RD


class InMemoryQueryBus(IQueryBus):
    def __init__(self) -> None:
        self.handlers: dict[type[Q], QH] = {}

    def register(self, query_class: type[Q], query_handler: QH) -> None:
        self.handlers[query_class] = query_handler

    def dispatch(self, query: Q) -> RD:
        handler: QH = self.handlers[type(query)]

        return handler.handle(query)
