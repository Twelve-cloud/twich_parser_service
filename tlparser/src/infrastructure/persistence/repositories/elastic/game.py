"""
game.py: File, containing twich game elastic repository implementation.
"""


from typing import Collection
from automapper import mapper
from application.exceptions import ObjectNotFoundException
from application.interfaces.repositories import ITwichGameRepository
from domain.models import TwichGame
from infrastructure.persistence.connections.elastic.database import ElasticSearchDatabase
from infrastructure.persistence.models.elastic.game import TwichGameDAO


class TwichGameElasticRepository(ITwichGameRepository):
    def __init__(self, db: ElasticSearchDatabase) -> None:
        self.db: ElasticSearchDatabase = db
        TwichGameDAO.init()

    async def add_or_update(self, game: TwichGame) -> None:
        game_persistence = mapper.to(TwichGameDAO).map(game)
        game_persistence.meta.id = game_persistence.id
        game_persistence.save()

        return

    async def all(self) -> list[TwichGame]:
        return [
            mapper.to(TwichGame).map(game_persistence)
            for game_persistence in TwichGameDAO.search().query()
        ]

    async def delete(self, game: TwichGame) -> None:
        TwichGameDAO.search().query('match', name=game.name).delete()

        return

    async def get_by_id(self, id: int) -> TwichGame:
        games: Collection[TwichGameDAO] = TwichGameDAO.search().query('match', id=id).execute()

        if len(games) == 0:
            raise ObjectNotFoundException('Game is not found.')

        return mapper.to(TwichGame).map(next(iter(games)))

    async def get_game_by_name(self, name: str) -> TwichGame:
        games: Collection[TwichGameDAO] = TwichGameDAO.search().query('match', name=name).execute()

        if len(games) == 0:
            raise ObjectNotFoundException('Game is not found.')

        return mapper.to(TwichGame).map(next(iter(games)))
