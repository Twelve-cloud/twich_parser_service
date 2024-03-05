"""
__init__.py: File, containing other parser modules to simplify import.
"""


from domain.interfaces.parsers.base import ITwichBaseParser
from domain.interfaces.parsers.game import ITwichGameParser
from domain.interfaces.parsers.stream import ITwichStreamParser
from domain.interfaces.parsers.user import ITwichUserParser


__all__: list[str] = [
    'ITwichBaseParser',
    'ITwichGameParser',
    'ITwichStreamParser',
    'ITwichUserParser',
]