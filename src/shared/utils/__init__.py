"""
__init__.py: File, containing other util modules to simplify import.
"""


from shared.utils.decorators import (
    ReadOnlyClassProperty,
    Singleton,
)


__all__: list[str] = [
    'ReadOnlyClassProperty',
    'Singleton',
]
