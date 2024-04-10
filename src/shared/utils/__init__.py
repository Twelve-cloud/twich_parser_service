"""
__init__.py: File, containing other util modules to simplify import.
"""


from shared.utils.decorators import (
    ReadOnlyClassProperty,
    Singleton,
    for_all_methods,
)


__all__: list[str] = [
    'ReadOnlyClassProperty',
    'Singleton',
    'for_all_methods',
]
