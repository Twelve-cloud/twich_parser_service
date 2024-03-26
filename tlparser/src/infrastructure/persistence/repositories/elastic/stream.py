"""
stream.py: File, containing twich stream elastic repository implementation.
"""


from typing import Collection
from automapper import mapper
from application.exceptions import ObjectNotFoundException
from application.interfaces.repository import ITwichStreamRepository
from domain.models import TwichStream
from infrastructure.persistence.connections.elastic.database import ElasticSearchDatabase
from infrastructure.persistence.models.elastic.stream import TwichStreamDAO


class TwichStreamElasticRepository(ITwichStreamRepository):
    def __init__(self, db: ElasticSearchDatabase) -> None:
        self.db: ElasticSearchDatabase = db
        TwichStreamDAO.init()

    async def add_or_update(self, stream: TwichStream) -> None:
        stream_persistence = mapper.to(TwichStreamDAO).map(stream)
        stream_persistence.meta.id = stream_persistence.id
        stream_persistence.save()

        return

    async def all(self) -> list[TwichStream]:
        return [
            mapper.to(TwichStream).map(stream_persistence)
            for stream_persistence in TwichStreamDAO.search().query()
        ]

    async def delete(self, stream: TwichStream) -> None:
        TwichStreamDAO.search().query('match', user_login=stream.user_login).delete()

        return

    async def get_by_id(self, id: int) -> TwichStream:
        streams: Collection[TwichStreamDAO] = (
            TwichStreamDAO.search()
            .query(
                'match',
                id=id,
            )
            .execute()
        )

        if len(streams) == 0:
            raise ObjectNotFoundException('Stream is not found.')

        return mapper.to(TwichStream).map(next(iter(streams)))

    async def get_stream_by_user_login(self, user_login: str) -> TwichStream:
        streams: Collection[TwichStreamDAO] = (
            TwichStreamDAO.search()
            .query(
                'match',
                user_login=user_login,
            )
            .execute()
        )

        if len(streams) == 0:
            raise ObjectNotFoundException('Stream is not found.')

        return mapper.to(TwichStream).map(next(iter(streams)))
