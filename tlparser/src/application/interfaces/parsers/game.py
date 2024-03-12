"""
game.py: File, containing parser interface for a twich game.
"""


from application.interfaces.parsers import ITwichParser
from domain.models import TwichGame


class ITwichGameParser(ITwichParser):
    async def parse_game(self, name: str) -> TwichGame:
        raise NotImplementedError
