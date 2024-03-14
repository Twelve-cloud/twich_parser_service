"""
game.py: File, containing repository interface for a twich game.
"""


from abc import abstractmethod
from application.interfaces.repositories.base import IRepository
from domain.models import TwichGame


class ITwichGameRepository(IRepository[TwichGame]):
    """
    ITwichGameRepository: Class, representing twich game repository interface.
    This class is an interface.

    Bases:
        1) IRepository[TwichGame]: Base repository interface.
           Every repository should be inherited from this class.
    """

    @abstractmethod
    async def get_game_by_name(self, name: str) -> TwichGame:
        """
        get_game_by_name: Should return twich game model instance by its name.
        Must be overriden.

        Args:
            name (str): Name of the game.

        Raises:
            NotImplementedError: Raises to prevent calling this method by super.

        Returns:
            TwichGame: Twich game domain model instance.
        """

        raise NotImplementedError
