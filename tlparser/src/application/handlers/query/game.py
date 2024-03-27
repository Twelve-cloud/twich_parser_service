"""
game.py: File, containing twich game query handlers.
"""


from automapper import mapper
from application.dto import TwichGameDTO, TwichGamesDTO
from application.interfaces.handler import IQueryHandler
from application.interfaces.repository import ITwichGameRepository
from application.queries import GetAllTwichGames, GetTwichGameByName
from domain.models import TwichGame


class GetTwichGameByNameHandler(IQueryHandler[GetTwichGameByName, TwichGameDTO]):
    def __init__(
        self,
        repository: ITwichGameRepository,
    ) -> None:
        self.repository: ITwichGameRepository = repository

    async def handle(self, query: GetTwichGameByName) -> TwichGameDTO:
        game: TwichGame = await self.repository.get_game_by_name(query.name)

        return mapper.to(TwichGameDTO).map(game)


class GetAllTwichGamesHandler(IQueryHandler[GetAllTwichGames, TwichGamesDTO]):
    def __init__(
        self,
        repository: ITwichGameRepository,
    ) -> None:
        self.repository: ITwichGameRepository = repository

    async def handle(self, query: GetAllTwichGames) -> TwichGamesDTO:
        games: list[TwichGame] = await self.repository.all()

        return TwichGamesDTO(data=[mapper.to(TwichGamesDTO).map(game) for game in games])
