"""
game.py: File, containing repository interface for a twich game.
"""


from abc import abstractmethod
from domain.interfaces.repositories import IBaseRepository
from domain.models import TwichGame


class ITwichGameRepository(IBaseRepository[TwichGame]):
    """
    ITwichGameRepository: Class that represents repository interface for a twich game.

    Args:
        IBaseRepository[TwichGame]: Base repository interface instantiated with twich game.
    """

    @abstractmethod
    async def get_game_by_name(self, name: str) -> TwichGame:
        """
        get_game_by_name: Should return game from a collection.
        Must be overriden.

        Args:
            name (str): Name of the game.

        Returns:
            TwichGame: Twich game domain model instance.
        """

        pass
