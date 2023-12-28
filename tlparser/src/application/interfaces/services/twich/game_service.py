"""
game_service.py: File, containing twich game service abstract class.
"""


from abc import abstractmethod
from application.interfaces.services.base.base_service import IBaseService
from application.schemas.twich.game_schema import TwichGameSchema


class ITwichGameService(IBaseService[TwichGameSchema]):
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
    async def private_parse_game(self, game_name: str) -> TwichGameSchema:
        """
        private_parse_game: Parse game data from the Twich.

        Args:
            game_name (str): Name of the game.

        Returns:
            TwichGameSchema: TwichGameSchema instance.
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
    async def get_all_games(self) -> list[TwichGameSchema]:
        """
        get_all_games: Return all twich games.

        Returns:
            list[TwichGameSchema]: List of twich games.
        """

        pass

    @abstractmethod
    async def get_game_by_name(self, game_name: str) -> TwichGameSchema:
        """
        get_game_by_name: Return twich game by name.

        Args:
            game_name (str): Name of the game.

        Returns:
            TwichGameSchema: TwichGameSchema instance.
        """

        pass
