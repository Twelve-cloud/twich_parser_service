"""
user.py: File, containing twich user elastic repository implementation.
"""


from typing import Collection
from automapper import mapper
from application.exceptions import ObjectNotFoundException
from application.interfaces.repositories import ITwichUserRepository
from domain.models import TwichUser
from infrastructure.persistence.connections.elastic.database import ElasticSearchDatabase
from infrastructure.persistence.models.elastic.user import TwichUserDAO


class TwichUserElasticRepository(ITwichUserRepository):
    def __init__(self, db: ElasticSearchDatabase) -> None:
        self.db: ElasticSearchDatabase = db
        TwichUserDAO.init()

    async def add_or_update(self, user: TwichUser) -> None:
        user_persistence = mapper.to(TwichUserDAO).map(user)
        user_persistence.meta.id = user_persistence.id
        user_persistence.save()

        return

    async def all(self) -> list[TwichUser]:
        return [
            mapper.to(TwichUser).map(user_persistence)
            for user_persistence in TwichUserDAO.search().query()
        ]

    async def delete(self, user: TwichUser) -> None:
        TwichUserDAO.search().query('match', login=user.login).delete()

        return

    async def get_by_id(self, id: int) -> TwichUser:
        users: Collection[TwichUserDAO] = (
            TwichUserDAO.search()
            .query(
                'match',
                id=id,
            )
            .execute()
        )

        if len(users) == 0:
            raise ObjectNotFoundException('User is not found.')

        return mapper.to(TwichUser).map(next(iter(users)))

    async def get_user_by_login(self, login: str) -> TwichUser:
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
