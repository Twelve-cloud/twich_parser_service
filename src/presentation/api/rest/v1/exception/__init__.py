"""
__init__.py: File, containing other exception modules to simplify import.
"""


from presentation.api.rest.v1.exception.handler import GlobalExceptionHandler


__all__: list[str] = [
    'GlobalExceptionHandler',
]
