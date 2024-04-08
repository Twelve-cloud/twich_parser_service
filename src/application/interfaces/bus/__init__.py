"""
__init__.py: File, containing other command bus interface modules to simplify import.
"""


from application.interfaces.bus.command_bus import ICommandBus
from application.interfaces.bus.query_bus import IQueryBus


__all__: list[str] = [
    'ICommandBus',
    'IQueryBus',
]
