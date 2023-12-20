"""
game_repository.py: File, containing twich game mongo repository implementation.
"""


from typing import Optional
from application.exceptions.twich.game_exceptions import GameNotFoundException
from domain.entities.twich.game_entity import TwichGameEntity
from domain.repositories.twich.game_repository import TwichGameRepository
from infrastructure.connections.mongo.database import MongoDatabase
from infrastructure.mappers.twich.mongo.game_mapper import TwichGameMapper
from infrastructure.models.twich.mongo.game_model import TwichGame


class TwichGameMongoRepository(TwichGameRepository):
    """
    TwichGameMongoRepository: Mongo implementation of TwichGameRepository.

    Args:
        TwichGameRepository (_type_): Repository abstract class.
    """

    def __init__(self, db: MongoDatabase) -> None:
        """
        __init__: Initialize repository.

        Args:
            db (MongoDatabase): MongoDatabase instance, containing mongo connection.
        """

        self.db = db

    def create_or_update(self, game_entity: TwichGameEntity) -> TwichGameEntity:
        """
        create_or_update: Create or update twich game.

        Args:
            game_entity (TwichGameEntity): Twich game entity.

        Returns:
            TwichGameEntity: Created/Updated twich game entity.
        """

        game_persistence = TwichGameMapper.to_persistence(game_entity)
        game_persistence.save()

        return TwichGameMapper.to_domain(game_persistence)

    def all(self) -> list[TwichGameEntity]:
        """
        all: Return list of twich games.

        Returns:
            list[TwichGameEntity]: List of twich games.
        """

        return [
            TwichGameMapper.to_domain(game_persistence) for game_persistence in TwichGame.objects
        ]

    def delete_game_by_name(self, name: str) -> None:
        """
        delete_game_by_name: Delete game by name.

        Args:
            name (str): Name of the game.
        """

        for game_persistence in TwichGame.objects(name=name):
            game_persistence.delete()

        return

    def get_game_by_name(self, name: str) -> TwichGameEntity:
        """
        get_game_by_name: Return game by name.

        Args:
            name (str): Name of the game.

        Returns:
            TwichGameEntity: Twich game entity.
        """

        game_persistence: Optional[TwichGame] = TwichGame.objects(name=name).first()

        if not game_persistence:
            raise GameNotFoundException

        return TwichGameMapper.to_domain(game_persistence)
