"""
game.py: File, containing parser interface for a twich game.
"""


from abc import abstractmethod
from domain.interfaces.parsers import ITwichBaseParser
from domain.models import TwichGame


class ITwichGameParser(ITwichBaseParser):
    """
    ITwichGameParser: Class that represents parser interface for a twich game.

    Args:
        ITwichBaseParser: Base twich parser interface.
    """

    @abstractmethod
    async def parse_game(self, name: str) -> TwichGame:
        """
        parse_game: Parse game data from the Twich, then create it and return.

        Args:
            name (str): Name of the game.

        Returns:
            TwichGame: Twich game domain model instance.
        """

        pass
