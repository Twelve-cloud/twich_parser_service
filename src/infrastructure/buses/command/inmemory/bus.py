"""
bus.py: File, containing in memory command bus implementation.
"""


from application.commands import Command
from application.dto import ResultDTO
from application.interfaces.bus import ICommandBus
from application.interfaces.handler import ICommandHandler


class InMemoryCommandBus(ICommandBus):
    def __init__(self) -> None:
        self.handlers: dict[type[Command], ICommandHandler] = {}

    def register(self, command_class: type[Command], command_handler: ICommandHandler) -> None:
        self.handlers[command_class] = command_handler

    async def dispatch(self, command: Command) -> ResultDTO:
        handler: ICommandHandler = self.handlers[type(command)]

        return await handler.handle(command)
