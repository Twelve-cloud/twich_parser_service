"""
game.py: File, containing parser interface for a twich game.
"""


from abc import abstractmethod
from application.interfaces.parsers import ITwichParser
from domain.models import TwichGame


class ITwichGameParser(ITwichParser):
    @abstractmethod
    async def parse_game(self, name: str) -> TwichGame:
        raise NotImplementedError
