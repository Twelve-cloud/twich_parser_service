"""
game.py: File, containing service interface for a twich game.
"""


from abc import abstractmethod
from application.dtos.requests import (
    DeleteTwichGameByNameRequest,
    GetTwichGameByNameRequest,
    ParseTwichGameRequest,
)
from application.dtos.responses import (
    DeleteTwichGameByNameResponse,
    GetTwichGameByNameResponse,
    ParseTwichGameResponse,
)
from application.interfaces.services import IBaseService


class ITwichGameService(IBaseService):
    """
    ITwichGameService: Class that represents service interface for a twich game.

    Args:
        IBaseService: Base service interface.
    """

    @abstractmethod
    async def parse_game(
        self,
        request: ParseTwichGameRequest,
    ) -> ParseTwichGameResponse:
        """
        parse_game: Should parse twich game.
        Must be overriden.

        Args:
            request (ParseTwichGameRequest): Request about parsing twich game.

        Returns:
            ParseTwichGameResponse: Response about parsing twich game.
        """

        pass

    @abstractmethod
    async def delete_game_by_name(
        self,
        request: DeleteTwichGameByNameRequest,
    ) -> DeleteTwichGameByNameResponse:
        """
        delete_game_by_name: Should delete twich game.
        Must be overriden.

        Args:
            request (DeleteTwichGameByNameRequest): Request about deleting twich game.

        Returns:
            DeleteTwichGameByNameResponse: Response about deleting twich game.
        """

        pass

    @abstractmethod
    async def get_all_games(
        self,
    ) -> list[GetTwichGameByNameResponse]:
        """
        get_all_games: Should return all twich games.
        Must be overriden.

        Returns:
            list[GetTwichGameByNameResponse]: List of responses about getting twich game.
        """

        pass

    @abstractmethod
    async def get_game_by_name(
        self,
        request: GetTwichGameByNameRequest,
    ) -> GetTwichGameByNameResponse:
        """
        get_game_by_name: Should return twich game.
        Must be overriden.

        Args:
            request (GetTwichGameByNameRequest): Request about getting twich game.

        Returns:
            GetTwichGameByNameResponse: Response about gettings twich game.
        """

        pass
