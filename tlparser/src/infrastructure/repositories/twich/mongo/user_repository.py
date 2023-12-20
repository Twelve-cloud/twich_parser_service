"""
user_repository.py: File, containing twich user mongo repository implementation.
"""


from typing import Optional
from application.exceptions.twich.user_exceptions import UserNotFoundException
from domain.entities.twich.user_entity import TwichUserEntity
from domain.repositories.twich.user_repository import TwichUserRepository
from infrastructure.connections.mongo.database import MongoDatabase
from infrastructure.mappers.twich.mongo.user_mapper import TwichUserMapper
from infrastructure.models.twich.mongo.user_model import TwichUser


class TwichUserMongoRepository(TwichUserRepository):
    """
    TwichUserMongoRepository: Mongo implementation of TwichUserRepository.

    Args:
        TwichUserRepository (_type_): Repository abstract class.
    """

    def __init__(self, db: MongoDatabase) -> None:
        """
        __init__: Initialize repository.

        Args:
            db (MongoDatabase): MongoDatabase instance, containing mongo connection.
        """

        self.db = db

    def create_or_update(self, user_entity: TwichUserEntity) -> TwichUserEntity:
        """
        create_or_update: Create or update twich user.

        Args:
            user_entity (TwichUserEntity): Twich user entity.

        Returns:
            TwichUserEntity: Created/Updated twich user entity.
        """

        user_persistence = TwichUserMapper.to_persistence(user_entity)
        user_persistence.save()

        return TwichUserMapper.to_domain(user_persistence)

    def all(self) -> list[TwichUserEntity]:
        """
        all: Return list of twich users.

        Returns:
            list[TwichUserEntity]: List of twich users.
        """

        return [
            TwichUserMapper.to_domain(user_persistence) for user_persistence in TwichUser.objects
        ]

    def delete_user_by_login(self, login: str) -> None:
        """
        delete_user_by_login: Delete user by login.

        Args:
            user_login (str): Login of the user.
        """

        for user_persistence in TwichUser.objects(login=login):
            user_persistence.delete()

        return

    def get_user_by_login(self, login: str) -> TwichUserEntity:
        """
        get_user_by_login: Return user by login.

        Args:
            user_login (str): Login of the user.

        Returns:
            TwichUserEntity: Twich user entity.
        """

        user_persistence: Optional[TwichUser] = TwichUser.objects(login=login).first()

        if not user_persistence:
            raise UserNotFoundException

        return TwichUserMapper.to_domain(user_persistence)
