"""
__init__.py: File, containing other handler interface modules to simplify import.
"""


from typing import TypeVar
from application.interfaces.handlers.command_handler import ICommandHandler
from application.interfaces.handlers.query_handler import IQueryHandler


CH = TypeVar('CH', bound=ICommandHandler)
QH = TypeVar('QH', bound=IQueryHandler)


__all__: list[str] = [
    'ICommandHandler',
    'IQueryHandler',
    'CH',
    'QH',
]
