"""
user.py: File, containing twich user mongo repository implementation.
"""


from typing import Optional
from automapper import mapper
from application.exceptions import ObjectNotFoundException
from application.interfaces.repositories import ITwichUserRepository
from domain.models import TwichUser
from infrastructure.persistence.connections.mongo.database import MongoDatabase
from infrastructure.persistence.models.mongo.user import TwichUserDAO


class TwichUserMongoRepository(ITwichUserRepository):
    def __init__(self, db: MongoDatabase) -> None:
        self.db: MongoDatabase = db

    async def add_or_update(self, user: TwichUser) -> None:
        user_persistence = mapper.to(TwichUserDAO).map(user)
        user_persistence.save()

        return

    async def all(self) -> list[TwichUser]:
        return [
            mapper.to(TwichUser).map(user_persistence) for user_persistence in TwichUserDAO.objects
        ]

    async def delete(self, user: TwichUser) -> None:
        for user_persistence in TwichUserDAO.objects(login=user.login):
            user_persistence.delete()

        return

    async def get_by_id(self, id: int) -> TwichUser:
        user_persistence: Optional[TwichUserDAO] = TwichUserDAO.objects(id=id).first()

        if not user_persistence:
            raise ObjectNotFoundException('User is not found.')

        return mapper.to(TwichUser).map(user_persistence)

    async def get_user_by_login(self, login: str) -> TwichUser:
        user_persistence: Optional[TwichUserDAO] = TwichUserDAO.objects(login=login).first()

        if not user_persistence:
            raise ObjectNotFoundException('User is not found.')

        return mapper.to(TwichUser).map(user_persistence)
