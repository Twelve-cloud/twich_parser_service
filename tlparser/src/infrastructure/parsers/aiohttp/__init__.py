"""
__init__.py: File, containing other parser modules to simplify import.
"""


from infrastructure.parsers.aiohttp.game import TwichGameParser
from infrastructure.parsers.aiohttp.stream import TwichStreamParser
from infrastructure.parsers.aiohttp.user import TwichUserParser


__all__: list[str] = [
    'TwichGameParser',
    'TwichStreamParser',
    'TwichUserParser',
]
