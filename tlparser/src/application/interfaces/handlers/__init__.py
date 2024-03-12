"""
__init__.py: File, containing other handler modules to simplify import.
"""


from application.interfaces.handlers.command_handler import ICommandHandler
from application.interfaces.handlers.query_handler import IQueryHandler


__all__: list[str] = [
    'ICommandHandler',
    'IQueryHandler',
]
