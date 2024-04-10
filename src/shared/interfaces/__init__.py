"""
__init__.py: File, containing other interface modules to simplify import.
"""


from shared.interfaces.exception_handler import IExceptionHandler
from shared.interfaces.logger import ILogger


__all__: list[str] = [
    'IExceptionHandler',
    'ILogger',
]
