"""
game.py: File, containing twich game query handlers.
"""


from automapper import mapper
from application import dto
from application.interfaces.handlers import IQueryHandler
from application.interfaces.repositories import ITwichGameRepository
from application.queries import GetAllTwichGames, GetTwichGameByName
from domain.models import TwichGame


class GetTwichGameByNameHandler(IQueryHandler[GetTwichGameByName, dto.TwichGame]):
    """
    GetTwichGameByNameHandler: Class, representing get twich game by name query handler.
    This class is interface implementation.

    Bases:
        1) IQueryHandler[GetTwichGameByName, dto.TwichGame]: Query handler interface.
           Every query handler should implement this class.
    """

    def __init__(
        self,
        repository: ITwichGameRepository,
    ) -> None:
        """
        __init__: Makes initialization.

        Args:
            repository (ITwichGameRepository): Twich game repository.
        """

        self.repository: ITwichGameRepository = repository

    async def handle(self, query: GetTwichGameByName) -> dto.TwichGame:
        """
        handle: Should handle get twich game by name query.
        Must be overriden.

        Args:
            query (GetTwichGameByName): Query.

        Returns:
            dto.TwichGame: Twich game.
        """

        game: TwichGame = await self.repository.get_game_by_name(query.name)

        return mapper.to(dto.TwichGame).map(game)


class GetAllTwichGamesHandler(IQueryHandler[GetAllTwichGames, dto.TwichGames]):
    """
    GetAllTwichGamesHandler: Class, representing get all twich games query handler.
    This class is interface implementation.

    Bases:
        1) IQueryHandler[GetAllTwichGames, dto.TwichGames]: Query handler interface.
           Every query handler should implement this class.
    """

    def __init__(
        self,
        repository: ITwichGameRepository,
    ) -> None:
        """
        __init__: Makes initialization.

        Args:
            repository (ITwichGameRepository): Twich game repository.
        """

        self.repository: ITwichGameRepository = repository

    async def handle(self, query: GetAllTwichGames) -> dto.TwichGames:
        """
        handle: Should handle get all twich games query.
        Must be overriden.

        Args:
            query (GetAllTwichGames): Query.

        Returns:
            dto.TwichGames: Twich games.
        """

        games: list[TwichGame] = await self.repository.all()

        return dto.TwichGames(data=[mapper.to(dto.TwichGame).map(game) for game in games])
