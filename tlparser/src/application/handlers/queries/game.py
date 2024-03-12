"""
game.py: File, containing twich game query handlers.
"""


from automapper import mapper
from application import dto
from application.interfaces.handlers import IQueryHandler
from application.interfaces.repositories import ITwichGameRepository
from application.queries import (
    GetAllTwichGames,
    GetTwichGameByName,
)
from domain.models import TwichGame


class GetTwichGameByNameHandler(IQueryHandler[GetTwichGameByName, dto.TwichGame]):
    def __init__(
        self,
        repository: ITwichGameRepository,
    ) -> None:
        self.repository: ITwichGameRepository = repository

    async def handle(self, query: GetTwichGameByName) -> dto.TwichGame:
        game: TwichGame = await self.repository.get_game_by_name(query.name)

        return mapper.to(dto.TwichGame).map(game)


class GetAllTwichGamesHandler(IQueryHandler[GetAllTwichGames, dto.TwichGames]):
    def __init__(
        self,
        repository: ITwichGameRepository,
    ) -> None:
        self.repository: ITwichGameRepository = repository

    async def handle(self, query: GetAllTwichGames) -> dto.TwichGames:
        games: list[TwichGame] = await self.repository.all()

        return dto.TwichGames(data=[mapper.to(dto.TwichGame).map(game) for game in games])
