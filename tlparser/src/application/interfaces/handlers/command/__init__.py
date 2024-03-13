"""
__init__.py: File, containing other command handler modules to simplify import.
"""


from application.interfaces.handlers.command.base import ICommandHandler


__all__: list[str] = [
    'ICommandHandler',
]
