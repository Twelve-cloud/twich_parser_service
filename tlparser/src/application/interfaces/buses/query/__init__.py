"""
__init__.py: File, containing other query bus modules to simplify import.
"""


from application.interfaces.buses.query.base import IQueryBus, Q, H, R


__all__: list[str] = [
    'IQueryBus',
    'Q',
    'H',
    'R',
]
