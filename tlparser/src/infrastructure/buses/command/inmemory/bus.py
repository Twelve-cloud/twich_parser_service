"""
bus.py: File, containing in memory command bus implementation.
"""


from application.interfaces.buses import ICommandBus
from application.commands import C
from application.interfaces.handlers import CH
from application.dto import Result


class InMemoryCommandBus(ICommandBus):
    def __init__(self) -> None:
        self.handlers: dict[type[C], CH] = {}

    def register(self, command_class: type[C], command_handler: CH) -> None:
        self.handlers[command_class] = command_handler

    def dispatch(self, command: C) -> Result:
        handler: CH = self.handlers[type(command)]

        return handler.handle(command)
