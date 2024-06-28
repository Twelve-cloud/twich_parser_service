"""
__init__.py: File, containing other interface modules to simplify import.
"""


from shared.interfaces.logger import ILogger


__all__: list[str] = [
    'IExceptionHandler',
    'ILogger',
]
