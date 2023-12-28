"""
stream_repository.py: File, containing twich stream elastic repository implementation.
"""


from typing import Collection
from domain.entities.twich.stream_entity import TwichStreamEntity
from domain.events.twich.stream_events import (
    PublicParseStreamCalledEvent,
    TwichStreamCreatedOrUpdatedEvent,
    TwichStreamDeletedByUserLoginEvent,
)
from domain.exceptions.twich.stream_exceptions import StreamNotFoundException
from domain.interfaces.repositories.twich.stream_repository import ITwichStreamRepository
from domain.types.types import ResultWithEvent
from infrastructure.connections.elastic.database import ElasticSearchDatabase
from infrastructure.mappers.twich.elastic.stream_mapper import TwichStreamMapper
from infrastructure.models.twich.elastic.stream_model import TwichStream


class TwichStreamElasticRepository(ITwichStreamRepository):
    """
    TwichStreamElasticRepository: Elastic implementation of ITwichStreamRepository.

    Args:
        ITwichStreamRepository (_type_): Repository abstract class.
    """

    def __init__(self, db: ElasticSearchDatabase) -> None:
        """
        __init__: Initialize repository.

        Args:
            db (ElasticSearchDatabase): ElasticDatabase instance, containing elastic connection.
        """

        self.db: ElasticSearchDatabase = db
        TwichStream.init()

    async def parse_stream(self, user_login: str) -> PublicParseStreamCalledEvent:
        """
        parse_stream: Return event about parsing twich stream.

        Args:
            user_login (str): Login of the user.

        Returns:
            PublicParseStreamCalledEvent: Event about parsing stream.
        """

        return PublicParseStreamCalledEvent(type='twich_stream', user_login=user_login)

    async def create_or_update(
        self, stream_entity: TwichStreamEntity
    ) -> ResultWithEvent[TwichStreamEntity, TwichStreamCreatedOrUpdatedEvent]:
        """
        create_or_update: Create or update twich stream.

        Args:
            stream_entity (TwichStreamEntity): Twich stream entity.

        Returns:
            ResultWithEvent[Result, Event]:: Created/Updated twich stream entity.
        """

        stream_persistence = TwichStreamMapper.to_persistence(stream_entity)
        stream_persistence.meta.id = stream_persistence.id
        stream_persistence.save()

        event: TwichStreamCreatedOrUpdatedEvent = TwichStreamCreatedOrUpdatedEvent(
            id=stream_persistence.id,
            user_id=stream_persistence.user_id,
            user_name=stream_persistence.user_name,
            user_login=stream_persistence.user_login,
            game_id=stream_persistence.game_id,
            game_name=stream_persistence.game_name,
            language=stream_persistence.language,
            title=stream_persistence.title,
            tags=[tag['tag'] for tag in stream_persistence.tags],
            started_at=stream_persistence.started_at,
            viewer_count=stream_persistence.viewer_count,
            type=stream_persistence.type,
            parsed_at=stream_persistence.parsed_at,
        )
        entity: TwichStreamEntity = TwichStreamMapper.to_domain(stream_persistence)

        return ResultWithEvent[TwichStreamEntity, TwichStreamCreatedOrUpdatedEvent](
            result=entity,
            event=event,
        )

    async def all(self) -> list[TwichStreamEntity]:
        """
        all: Return list of twich streams.

        Returns:
            list[TwichStreamEntity]: List of twich streams.
        """

        return [
            TwichStreamMapper.to_domain(stream_persistence)
            for stream_persistence in TwichStream.search().query()
        ]

    async def delete_stream_by_user_login(
        self,
        user_login: str,
    ) -> TwichStreamDeletedByUserLoginEvent:
        """
        delete_stream_by_user_login: Delete stream by user login.

        Args:
            user_login (str): Login of the user.

        Returns:
            TwichStreamDeletedByUserLoginEvent: Twich stream deleted event.
        """

        TwichStream.search().query('match', user_login=user_login).delete()

        return TwichStreamDeletedByUserLoginEvent(user_login=user_login)

    async def get_stream_by_user_login(self, user_login: str) -> TwichStreamEntity:
        """
        get_stream_by_user_login: Return stream by user login.

        Args:
            user_login (str): Login of the user.

        Returns:
            TwichStreamEntity: Twich stream entity.
        """

        streams: Collection[TwichStream] = (
            TwichStream.search()
            .query(
                'match',
                user_login=user_login,
            )
            .execute()
        )

        if len(streams) == 0:
            raise StreamNotFoundException

        return TwichStreamMapper.to_domain(next(iter(streams)))
