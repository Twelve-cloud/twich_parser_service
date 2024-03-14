"""
game.py: File, containing parser interface for a twich game.
"""


from abc import abstractmethod
from application.interfaces.parsers.base import IParser
from domain.models import TwichGame


class ITwichGameParser(IParser):
    """
    ITwichGameParser: Class, representing twich game parser interface.
    This class is an interface.

    Bases:
        1) IParser: Base parser interface. Every parser should be inherited from this class.
    """

    @abstractmethod
    async def parse_game(self, name: str) -> TwichGame:
        """
        parse_game: Should parse game.
        Must be overriden.

        Args:
            name (str): Name of the game.

        Raises:
            NotImplementedError: Raises to prevent calling this method by super.

        Returns:
            TwichGame: Twich game domain model instance.
        """

        raise NotImplementedError
