"""
__init__.py: File, containing other handler modules to simplify import.
"""


from application.exceptions.handlers.domain_exception_handler import DomainExceptionHandler


__all__: list[str] = [
    'DomainExceptionHandler',
]
