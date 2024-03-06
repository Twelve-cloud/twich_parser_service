"""
user.py: File, containing twich user elastic repository implementation.
"""


from typing import Collection
from automapper import mapper
from domain.exceptions import ObjectNotFoundException
from domain.interfaces.repositories import ITwichUserRepository
from domain.models import TwichUser
from infrastructure.persistence.connections.elastic.database import ElasticSearchDatabase
from infrastructure.persistence.models.elastic.user import TwichUserDAO


class TwichUserElasticRepository(ITwichUserRepository):
    """
    TwichUserElasticRepository: Elastic implementation of ITwichUserRepository.

    Args:
        ITwichUserRepository: Repository abstract class.
    """

    def __init__(self, db: ElasticSearchDatabase) -> None:
        """
        __init__: Initialize repository.

        Args:
            db (ElasticSearchDatabase): ElasticDatabase instance, containing elastic connection.
        """

        self.db: ElasticSearchDatabase = db
        TwichUserDAO.init()

    async def add_or_update(self, user: TwichUser) -> None:
        """
        add_or_update: Add or update twich user.

        Args:
            user (TwichUser): Twich user.
        """

        user_persistence = mapper.to(TwichUserDAO).map(user)
        user_persistence.meta.id = user_persistence.id
        user_persistence.save()

        return

    async def all(self) -> list[TwichUser]:
        """
        all: Return list of twich users.

        Returns:
            list[TwichUser]: List of twich users.
        """

        return [
            mapper.to(TwichUser).map(user_persistence)
            for user_persistence in TwichUserDAO.search().query()
        ]

    async def delete(self, user: TwichUser) -> None:
        """
        delete: Delete twich user by login.

        Args:
            user (TwichUser): Twich user.
        """

        TwichUserDAO.search().query('match', login=user.login).delete()

        return

    async def get_user_by_login(self, login: str) -> TwichUser:
        """
        get_user_by_login: Return twich user by login.

        Args:
            user_login (str): Login of the user.

        Returns:
            TwichUser: Twich user.
        """

        users: Collection[TwichUserDAO] = (
            TwichUserDAO.search()
            .query(
                'match',
                login=login,
            )
            .execute()
        )

        if len(users) == 0:
            raise ObjectNotFoundException('User is not found.')

        return mapper.to(TwichUser).map(next(iter(users)))
