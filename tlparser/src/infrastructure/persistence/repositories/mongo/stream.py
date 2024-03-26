"""
stream.py: File, containing twich stream mongo repository implementation.
"""


from typing import Optional
from automapper import mapper
from application.exceptions import ObjectNotFoundException
from application.interfaces.repository import ITwichStreamRepository
from domain.models import TwichStream
from infrastructure.persistence.connections.mongo.database import MongoDatabase
from infrastructure.persistence.models.mongo.stream import TwichStreamDAO


class TwichStreamMongoRepository(ITwichStreamRepository):
    def __init__(self, db: MongoDatabase) -> None:
        self.db: MongoDatabase = db

    async def add_or_update(self, stream: TwichStream) -> None:
        stream_persistence = mapper.to(TwichStreamDAO).map(stream)
        stream_persistence.save()

        return

    async def all(self) -> list[TwichStream]:
        return [
            mapper.to(TwichStream).map(stream_persistence)
            for stream_persistence in TwichStreamDAO.objects
        ]

    async def delete(self, stream: TwichStream) -> None:
        for stream_persistence in TwichStreamDAO.objects(user_login=stream.user_login):
            stream_persistence.delete()

        return

    async def get_by_id(self, id: int) -> TwichStream:
        stream_persistence: Optional[TwichStreamDAO] = TwichStreamDAO.objects(
            id=id,
        ).first()

        if not stream_persistence:
            raise ObjectNotFoundException('Stream is not found.')

        return mapper.to(TwichStream).map(stream_persistence)

    async def get_stream_by_user_login(self, user_login: str) -> TwichStream:
        stream_persistence: Optional[TwichStreamDAO] = TwichStreamDAO.objects(
            user_login=user_login,
        ).first()

        if not stream_persistence:
            raise ObjectNotFoundException('Stream is not found.')

        return mapper.to(TwichStream).map(stream_persistence)
