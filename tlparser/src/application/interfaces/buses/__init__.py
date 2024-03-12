"""
__init__.py: File, containing other bus modules to simplify import.
"""


from application.interfaces.buses.command_bus import ICommandBus
from application.interfaces.buses.query_bus import IQueryBus


__all__: list[str] = [
    'ICommandBus',
    'IQueryBus',
]
