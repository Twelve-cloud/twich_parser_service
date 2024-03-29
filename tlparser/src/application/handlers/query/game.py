"""
game.py: File, containing twich game query handlers.
"""


from dataclasses import asdict
from application.dto import TwichGameDTO, TwichGamesDTO
from application.interfaces.handler import IQueryHandler
from application.interfaces.repository import ITwichGameRepository
from application.queries import (
    GetAllTwichGames,
    GetTwichGame,
    GetTwichGameByName,
)
from domain.models import TwichGame


class GetTwichGameHandler(IQueryHandler[GetTwichGame, TwichGameDTO]):
    def __init__(
        self,
        repository: ITwichGameRepository,
    ) -> None:
        self.repository: ITwichGameRepository = repository

    async def handle(self, query: GetTwichGame) -> TwichGameDTO:
        game: TwichGame = await self.repository.get_by_id(query.id)

        return TwichGameDTO(**asdict(game, dict_factory=TwichGame.dict))


class GetTwichGameByNameHandler(IQueryHandler[GetTwichGameByName, TwichGameDTO]):
    def __init__(
        self,
        repository: ITwichGameRepository,
    ) -> None:
        self.repository: ITwichGameRepository = repository

    async def handle(self, query: GetTwichGameByName) -> TwichGameDTO:
        game: TwichGame = await self.repository.get_game_by_name(query.name)

        return TwichGameDTO(**asdict(game, dict_factory=TwichGame.dict))


class GetAllTwichGamesHandler(IQueryHandler[GetAllTwichGames, TwichGamesDTO]):
    def __init__(
        self,
        repository: ITwichGameRepository,
    ) -> None:
        self.repository: ITwichGameRepository = repository

    async def handle(self, query: GetAllTwichGames) -> TwichGamesDTO:
        games: list[TwichGame] = await self.repository.all()

        return TwichGamesDTO(
            [TwichGameDTO(**asdict(game, dict_factory=TwichGame.dict)) for game in games]
        )
