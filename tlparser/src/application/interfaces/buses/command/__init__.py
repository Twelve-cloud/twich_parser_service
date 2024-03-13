"""
__init__.py: File, containing other command bus modules to simplify import.
"""


from application.interfaces.buses.command.base import ICommandBus


__all__: list[str] = [
    'ICommandBus',
]
