"""
game_service.py: File, containing twich game service abstract class.
"""


from abc import abstractmethod
from domain.entities.twich.game_entity import TwichGameEntity
from domain.services.base.base_service import IBaseService


class ITwichGameService(IBaseService):
    """
    ITwichGameService: Class, that represents abstract class for twich game service.

    Args:
        IBaseService (_type_): Base abstract class for twich game abstract class.
    """

    @abstractmethod
    async def parse_game(self, game_name: str) -> None:
        """
        parse_game: Called twich game publisher to publish event about parsing.

        Args:
            game_name (str): Name of the game.
        """

        pass

    @abstractmethod
    async def private_parse_game(self, game_name: str) -> TwichGameEntity:
        """
        private_parse_game: Parse game data from the Twich.

        Args:
            game_name (str): Name of the game.

        Returns:
            TwichGameEntity: TwichGameEntity instance.
        """

        pass

    @abstractmethod
    async def delete_game_by_name(self, game_name: str) -> None:
        """
        delete_game_by_name: Delete twich game.

        Args:
            game_name (str): Name of the game.
        """

        pass

    @abstractmethod
    async def get_all_games(self) -> list[TwichGameEntity]:
        """
        get_all_games: Return all twich games.

        Returns:
            list[TwichGameEntity]: List of twich games.
        """

        pass

    @abstractmethod
    async def get_game_by_name(self, game_name: str) -> TwichGameEntity:
        """
        get_game_by_name: Return twich game by name.

        Args:
            game_name (str): Name of the game.

        Returns:
            TwichGameEntity: TwichGameEntity instance.
        """

        pass
