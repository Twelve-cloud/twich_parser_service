"""
__init__.py: File, containing other query handler modules to simplify import.
"""


from application.interfaces.handlers.query.base import IQueryHandler


__all__: list[str] = [
    'IQueryHandler',
]
