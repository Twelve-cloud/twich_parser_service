"""
game.py: File, containing parser interface for a twich game.
"""


from domain.interfaces.parsers import ITwichParser
from domain.models import TwichGame


class ITwichGameParser(ITwichParser):
    async def parse_game(self, name: str) -> TwichGame:
        pass
