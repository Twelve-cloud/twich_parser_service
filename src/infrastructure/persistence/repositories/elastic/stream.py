"""
stream.py: File, containing twich stream elastic repository implementation.
"""


from typing import Collection

from application.exceptions import ObjectNotFoundException
from application.interfaces.repository import ITwichStreamRepository
from domain.models import TwichStream
from infrastructure.persistence.connections.elastic.database import ElasticSearchDatabase
from infrastructure.persistence.models.elastic.stream import (
    Tag,
    TwichStreamDAO,
)


class TwichStreamElasticRepository(ITwichStreamRepository):
    def __init__(self, db: ElasticSearchDatabase) -> None:
        self.db: ElasticSearchDatabase = db
        TwichStreamDAO.init()

    async def add_or_update(self, stream: TwichStream) -> None:
        tags = []

        for tag in stream.tags:
            tags.append(Tag(tag=tag))

        stream_persistence = TwichStreamDAO(
            id=stream.id,
            user_id=stream.user_id,
            user_name=stream.user_name,
            user_login=stream.user_login,
            game_id=stream.game_id,
            game_name=stream.game_name,
            language=stream.language,
            title=stream.title,
            tags=tags,
            started_at=stream.started_at,
            viewer_count=stream.viewer_count,
            type=stream.type,
            parsed_at=stream.parsed_at,
        )
        stream_persistence.meta.id = stream_persistence.id
        stream_persistence.save()

        return

    async def all(self) -> list[TwichStream]:
        streams = []

        for stream in TwichStreamDAO.search().query():
            tags = []

            for tag in stream.tags:
                tags.append(tag['tag'])

            streams.append(
                TwichStream(
                    id=stream.id,
                    user_id=stream.user_id,
                    user_name=stream.user_name,
                    user_login=stream.user_login,
                    game_id=stream.game_id,
                    game_name=stream.game_name,
                    language=stream.language,
                    title=stream.title,
                    tags=tags,
                    started_at=stream.started_at,
                    viewer_count=stream.viewer_count,
                    type=stream.type,
                    parsed_at=stream.parsed_at,
                )
            )

        return streams

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

        stream = next(iter(streams))

        tags = []

        for tag in stream.tags:
            tags.append(tag['tag'])

        return TwichStream(
            id=stream.id,
            user_id=stream.user_id,
            user_name=stream.user_name,
            user_login=stream.user_login,
            game_id=stream.game_id,
            game_name=stream.game_name,
            language=stream.language,
            title=stream.title,
            tags=tags,
            started_at=stream.started_at,
            viewer_count=stream.viewer_count,
            type=stream.type,
            parsed_at=stream.parsed_at,
        )

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

        stream = next(iter(streams))

        tags = []

        for tag in stream.tags:
            tags.append(tag['tag'])

        return TwichStream(
            id=stream.id,
            user_id=stream.user_id,
            user_name=stream.user_name,
            user_login=stream.user_login,
            game_id=stream.game_id,
            game_name=stream.game_name,
            language=stream.language,
            title=stream.title,
            tags=tags,
            started_at=stream.started_at,
            viewer_count=stream.viewer_count,
            type=stream.type,
            parsed_at=stream.parsed_at,
        )
