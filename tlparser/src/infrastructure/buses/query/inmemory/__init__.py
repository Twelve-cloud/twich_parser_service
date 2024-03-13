"""
__init__.py: File, containing other in memory query bus modules to simplify import.
"""


from infrastructure.buses.query.inmemory.bus import InMemoryQueryBus


__all__: list[str] = [
    'InMemoryQueryBus',
]
