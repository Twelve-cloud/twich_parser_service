"""
__init__.py: File, containing other exception handler modules to simplify import.
"""


from application.interfaces.handlers.exceptions.exception_handler import IExceptionHandler


__all__: list[str] = [
    'IExceptionHandler',
]
