"""
__init__.py: File, containing other parser interface modules to simplify import.
"""


from application.interfaces.parsers.base import IParser
from application.interfaces.parsers.game import ITwichGameParser
from application.interfaces.parsers.stream import ITwichStreamParser
from application.interfaces.parsers.user import ITwichUserParser


__all__: list[str] = [
    'IParser',
    'ITwichGameParser',
    'ITwichStreamParser',
    'ITwichUserParser',
]
