"""
bus.py: File, containing in memory command bus implementation.
"""


from application.interfaces.buses.command import ICommandBus, C, H
from application.dto import Result


class InMemoryCommandBus(ICommandBus):
    def __init__(self) -> None:
        self.handlers: dict[type[C], H] = {}

    def register(self, command_class: type[C], command_handler: H) -> None:
        self.handlers[command_class] = command_handler

    def execute(self, command: C) -> Result:
        handler: H = self.handlers[type[command]]

        return handler.handle(command)
