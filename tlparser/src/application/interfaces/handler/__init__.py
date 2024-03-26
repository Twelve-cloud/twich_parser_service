"""
__init__.py: File, containing other handler interface modules to simplify import.
"""


from application.interfaces.handler.command_handler import ICommandHandler
from application.interfaces.handler.query_handler import IQueryHandler


__all__: list[str] = [
    'ICommandHandler',
    'IQueryHandler',
]
