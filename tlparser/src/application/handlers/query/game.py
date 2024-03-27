"""
game.py: File, containing twich game query handlers.
"""


from dataclasses import asdict
from application.dto import TwichGameDTO
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

        return TwichGameDTO(**asdict(game, dict_factory=TwichGame.as_dict))


class GetAllTwichGamesHandler(IQueryHandler[GetAllTwichGames, list[TwichGameDTO]]):
    def __init__(
        self,
        repository: ITwichGameRepository,
    ) -> None:
        self.repository: ITwichGameRepository = repository

    async def handle(self, query: GetAllTwichGames) -> list[TwichGameDTO]:
        games: list[TwichGame] = await self.repository.all()

        return [TwichGameDTO(**asdict(game, dict_factory=TwichGame.as_dict)) for game in games]
