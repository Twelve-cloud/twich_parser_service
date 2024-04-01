"""
game.py: File, containing twich game mongo repository implementation.
"""


from typing import Optional

from automapper import mapper

from application.exceptions import ObjectNotFoundException
from application.interfaces.repository import ITwichGameRepository
from domain.models import TwichGame
from infrastructure.persistence.connections.mongo.database import MongoDatabase
from infrastructure.persistence.models.mongo.game import TwichGameDAO


class TwichGameMongoRepository(ITwichGameRepository):
    def __init__(self, db: MongoDatabase) -> None:
        self.db: MongoDatabase = db

    async def add_or_update(self, game: TwichGame) -> None:
        game_persistence = TwichGameDAO(
            id=game.id,
            name=game.name,
            igdb_id=game.igdb_id,
            box_art_url=game.box_art_url,
            parsed_at=game.parsed_at,
        )
        game_persistence.save()

        return

    async def all(self) -> list[TwichGame]:
        return [
            mapper.to(TwichGame).map(game_persistence) for game_persistence in TwichGameDAO.objects
        ]

    async def delete(self, game: TwichGame) -> None:
        for game_persistence in TwichGameDAO.objects(name=game.name):
            game_persistence.delete()

        return

    async def get_by_id(self, id: int) -> TwichGame:
        game_persistence: Optional[TwichGameDAO] = TwichGameDAO.objects(id=id).first()

        if not game_persistence:
            raise ObjectNotFoundException('Game is not found.')

        return mapper.to(TwichGame).map(game_persistence)

    async def get_game_by_name(self, name: str) -> TwichGame:
        game_persistence: Optional[TwichGameDAO] = TwichGameDAO.objects(name=name).first()

        if not game_persistence:
            raise ObjectNotFoundException('Game is not found.')

        return mapper.to(TwichGame).map(game_persistence)
