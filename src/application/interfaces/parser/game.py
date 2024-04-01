"""
game.py: File, containing parser interface for a twich game.
"""


from abc import abstractmethod

from application.interfaces.parser.base import IParser
from domain.models import TwichGame


class ITwichGameParser(IParser):
    @abstractmethod
    async def parse_game(self, name: str) -> TwichGame:
        raise NotImplementedError
