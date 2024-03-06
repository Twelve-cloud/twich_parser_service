"""
game.py: File, containing twich game mongo repository implementation.
"""


from typing import Optional
from automapper import mapper
from domain.exceptions import ObjectNotFoundException
from domain.interfaces.repositories import ITwichGameRepository
from domain.models import TwichGame
from infrastructure.persistence.connections.mongo.database import MongoDatabase
from infrastructure.persistence.models.mongo.game import TwichGameDAO


class TwichGameMongoRepository(ITwichGameRepository):
    """
    TwichGameMongoRepository: Mongo implementation of ITwichGameRepository.

    Args:
        ITwichGameRepository (_type_): Repository abstract class.
    """

    def __init__(self, db: MongoDatabase) -> None:
        """
        __init__: Initialize repository.

        Args:
            db (MongoDatabase): MongoDatabase instance, containing mongo connection.
        """

        self.db: MongoDatabase = db

    async def add_or_update(self, game: TwichGame) -> None:
        """
        add_or_update: Add or update twich game.

        Args:
            game (TwichGame): Twich game.
        """

        game_persistence = mapper.to(TwichGameDAO).map(game)
        game_persistence.save()

        return

    async def all(self) -> list[TwichGame]:
        """
        all: Return list of twich games.

        Returns:
            list[TwichGame]: List of twich games.
        """

        return [
            mapper.to(TwichGame).map(game_persistence) for game_persistence in TwichGameDAO.objects
        ]

    async def delete(self, game: TwichGame) -> None:
        """
        delete: Delete twich game by name.

        Args:
            game (TwichGame): Twich game.
        """

        for game_persistence in TwichGameDAO.objects(name=game.name):
            game_persistence.delete()

        return

    async def get_game_by_name(self, name: str) -> TwichGame:
        """
        get_game_by_name: Return twich game by name.

        Args:
            name (str): Name of the game.

        Returns:
            TwichGame: Twich game.
        """

        game_persistence: Optional[TwichGameDAO] = TwichGameDAO.objects(name=name).first()

        if not game_persistence:
            raise ObjectNotFoundException('Game is not found.')

        return mapper.to(TwichGame).map(game_persistence)
