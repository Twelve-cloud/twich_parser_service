"""
bus.py: File, containing in memory query bus implementation.
"""


from application.interfaces.buses.query import IQueryBus, Q, H, R


class InMemoryQueryBus(IQueryBus):
    def __init__(self) -> None:
        self.handlers: dict[type[Q], H] = {}

    def register(self, query_class: type[Q], query_handler: H) -> None:
        self.handlers[query_class] = query_handler

    def execute(self, query: Q) -> R:
        handler: H = self.handlers[type[query]]

        return handler.handle(query)
