"""
__init__.py: File, containing other interface modules to simplify import.
"""


from common.interfaces.exception_handler import IExceptionHandler
from common.interfaces.logger import ILogger


__all__: list[str] = [
    'IExceptionHandler',
    'ILogger',
]
