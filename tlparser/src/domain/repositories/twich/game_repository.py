"""
game_repository.py: File, containing repository abstract class for a twich game.
"""


from abc import abstractmethod
from domain.entities.twich.game_entity import TwichGameEntity
from domain.repositories.base.base_repository import BaseRepository


class TwichGameRepository(BaseRepository[TwichGameEntity]):
    """
    TwichGameRepository: Abstract class for twich game repositories.

    Args:
        BaseRepository (TwichGameEntity): BaseRepository for TwichGameRepository.
    """

    @abstractmethod
    def delete_game_by_name(self, name: str) -> None:
        """
        delete_game_by_name: Delete game by name.

        Args:
            name (str): Name of the game.
        """

        pass

    @abstractmethod
    def get_game_by_name(self, name: str) -> TwichGameEntity:
        """
        get_game_by_name: Return game by name.

        Args:
            name (str): Name of the game.

        Returns:
            TwichGameEntity: Twich game entity.
        """

        pass
