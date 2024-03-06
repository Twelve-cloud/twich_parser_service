"""
__init__.py: File, containing other exception handler modules to simplify import.
"""


from application.handlers.exceptions.domain_exception_handler import DomainExceptionHandler


__all__: list[str] = [
    'DomainExceptionHandler',
]
