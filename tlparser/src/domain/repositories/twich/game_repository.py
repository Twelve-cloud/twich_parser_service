"""
game_repository.py: File, containing repository abstract class for a twich game.
"""


from abc import abstractmethod
from domain.entities.twich.game_entity import TwichGameEntity
from domain.events.twich.game_events import (
    PublicParseGameCalledEvent,
    TwichGameCreatedOrUpdatedEvent,
    TwichGameDeletedByNameEvent,
)
from domain.repositories.base.base_repository import IBaseRepository


class ITwichGameRepository(IBaseRepository[TwichGameEntity, TwichGameCreatedOrUpdatedEvent]):
    """
    ITwichGameRepository: Abstract class for twich game repositories.

    Args:
        IBaseRepository (TwichGameEntity): IBaseRepository for ITwichGameRepository.
    """

    @abstractmethod
    def parse_game(self, name: str) -> PublicParseGameCalledEvent:
        """
        parse_game: Return event about parsing twich game.

        Args:
            name (str): Name of the game.

        Returns:
            PublicParseGameCalledEvent: Event about parsing twich game.
        """

        pass

    @abstractmethod
    def delete_game_by_name(self, name: str) -> TwichGameDeletedByNameEvent:
        """
        delete_game_by_name: Delete game by name.

        Args:
            name (str): Name of the game.

        Returns:
            TwichGameDeletedByNameEvent: Event about deleting twich game.
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
