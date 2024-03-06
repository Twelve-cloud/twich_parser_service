"""
user.py: File, containing twich user mongo repository implementation.
"""


from typing import Optional
from automapper import mapper
from domain.exceptions import ObjectNotFoundException
from domain.interfaces.repositories import ITwichUserRepository
from domain.models import TwichUser
from infrastructure.persistence.connections.mongo.database import MongoDatabase
from infrastructure.persistence.models.mongo.user import TwichUserDAO


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

    async def add_or_update(self, user: TwichUser) -> None:
        """
        add_or_update: Add or update twich user.

        Args:
            user (TwichUser): Twich user.
        """

        user_persistence = mapper.to(TwichUserDAO).map(user)
        user_persistence.save()

        return

    async def all(self) -> list[TwichUser]:
        """
        all: Return list of twich users.

        Returns:
            list[TwichUser]: List of twich users.
        """

        return [
            mapper.to(TwichUser).map(user_persistence) for user_persistence in TwichUserDAO.objects
        ]

    async def delete(self, user: TwichUser) -> None:
        """
        delete: Delete twich user by login.

        Args:
            user (TwichUser): Twich user.
        """

        for user_persistence in TwichUserDAO.objects(login=user.login):
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
            raise ObjectNotFoundException('User is not found.')

        return mapper.to(TwichUser).map(user_persistence)
