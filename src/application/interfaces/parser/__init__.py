"""
__init__.py: File, containing other parser interface modules to simplify import.
"""


from application.interfaces.parser.base import IParser
from application.interfaces.parser.game import ITwichGameParser
from application.interfaces.parser.stream import ITwichStreamParser
from application.interfaces.parser.user import ITwichUserParser


__all__: list[str] = [
    'IParser',
    'ITwichGameParser',
    'ITwichStreamParser',
    'ITwichUserParser',
]
