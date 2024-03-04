"""
user.py: File, containing twich user mongo repository implementation.
"""


from typing import Optional
from domain.exceptions.user import UserNotFoundException
from domain.exceptions.repositories.user import ITwichUserRepository
from domain.models.user import TwichUser
from infrastructure.connections.mongo.database import MongoDatabase
from infrastructure.mappers.twich.mongo.user_mapper import TwichUserMapper
from infrastructure.models.twich.mongo.user_model import TwichUserDAO


class TwichUserMongoRepository(ITwichUserRepository):
    """
    TwichUserMongoRepository: Mongo implementation of ITwichUserRepository.

    Args:
        ITwichUserRepository (_type_): Repository abstract class.
    """

    def __init__(self, db: MongoDatabase) -> None:
        """
        __init__: Initialize repository.

        Args:
            db (MongoDatabase): MongoDatabase instance, containing mongo connection.
        """

        self.db: MongoDatabase = db

    async def create_or_update(self, user: TwichUser) -> None:
        """
        create_or_update: Create or update twich user.

        Args:
            user (TwichUser): Twich user.
        """

        user_persistence = TwichUserMapper.to_persistence(user)
        user_persistence.save()

        return

    async def all(self) -> list[TwichUser]:
        """
        all: Return list of twich users.

        Returns:
            list[TwichUser]: List of twich users.
        """

        return [
            TwichUserMapper.to_domain(user_persistence) for user_persistence in TwichUserDAO.objects
        ]

    async def delete_user_by_login(self, login: str) -> None:
        """
        delete_user_by_login: Delete twich user by login.

        Args:
            user_login (str): Login of the user.

        Returns:
            TwichUserDeletedByLoginEvent: Twich user deleted event.
        """

        for user_persistence in TwichUserDAO.objects(login=login):
            user_persistence.delete()

        return

    async def get_user_by_login(self, login: str) -> TwichUser:
        """
        get_user_by_login: Return twich user by login.

        Args:
            user_login (str): Login of the user.

        Returns:
            TwichUser: Twich user .
        """

        user_persistence: Optional[TwichUserDAO] = TwichUserDAO.objects(login=login).first()

        if not user_persistence:
            raise UserNotFoundException

        return TwichUserMapper.to_domain(user_persistence)
