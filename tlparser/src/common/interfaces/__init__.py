"""
__init__.py: File, containing other interface modules to simplify import.
"""


from common.interfaces.decorator import IDecorator
from common.interfaces.exception_handler import IExceptionHandler
from common.interfaces.logger import ILogger


__all__: list[str] = [
    'IDecorator',
    'IExceptionHandler',
    'ILogger',
]
