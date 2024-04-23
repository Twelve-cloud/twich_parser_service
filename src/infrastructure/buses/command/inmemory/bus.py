"""
bus.py: File, containing in memory command bus implementation.
"""


from application.commands import Command
from application.dto import ResultDTO
from application.interfaces.bus import ICommandBus
from application.interfaces.handler import ICommandHandler


class InMemoryCommandBus(ICommandBus):
    def __init__(self, command_handlers: dict[type[Command], ICommandHandler]) -> None:
        self._command_handlers: dict[type[Command], ICommandHandler] = command_handlers

    def register(self, command_class: type[Command], command_handler: ICommandHandler) -> None:
        self._command_handlers[command_class] = command_handler

    async def dispatch(self, command: Command) -> ResultDTO:
        handler: ICommandHandler = self._command_handlers[type(command)]

        return await handler.handle(command)
