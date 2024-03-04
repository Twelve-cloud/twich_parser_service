"""
game.py: File, containing twich game mongo repository implementation.
"""


from typing import Optional
from domain.exceptions.game import GameNotFoundException
from domain.exceptions.repositories.game import ITwichGameRepository
from domain.models.game import TwichGame
from infrastructure.connections.mongo.database import MongoDatabase
from infrastructure.mappers.twich.mongo.game_mapper import TwichGameMapper
from infrastructure.models.twich.mongo.game_model import TwichGameDAO


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
        create_or_update: Create or update twich game.

        Args:
            game (TwichGame): Twich game.
        """

        game_persistence = TwichGameMapper.to_persistence(game)
        game_persistence.save()

        return

    async def all(self) -> list[TwichGame]:
        """
        all: Return list of twich games.

        Returns:
            list[TwichGame]: List of twich games.
        """

        return [
            TwichGameMapper.to_domain(game_persistence) for game_persistence in TwichGameDAO.objects
        ]

    async def delete_game_by_name(self, name: str) -> None:
        """
        delete_game_by_name: Delete twich game by name.

        Args:
            name (str): Name of the game.
        """

        for game_persistence in TwichGameDAO.objects(name=name):
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
            raise GameNotFoundException

        return TwichGameMapper.to_domain(game_persistence)
