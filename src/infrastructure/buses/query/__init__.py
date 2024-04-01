"""
__init__.py: File, containing other query bus modules to simplify import.
"""


from infrastructure.buses.query.inmemory import InMemoryQueryBus


__all__: list[str] = [
    'InMemoryQueryBus',
]
