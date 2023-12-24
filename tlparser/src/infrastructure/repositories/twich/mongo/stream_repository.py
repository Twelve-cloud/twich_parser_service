"""
stream_repository.py: File, containing twich stream mongo repository implementation.
"""


from typing import Optional
from application.exceptions.twich.stream_exceptions import StreamNotFoundException
from domain.entities.twich.stream_entity import TwichStreamEntity
from domain.events.twich.stream_events import (
    PublicParseStreamCalledEvent,
    TwichStreamCreatedOrUpdatedEvent,
    TwichStreamDeletedByUserLoginEvent,
)
from domain.repositories.base.base_repository import ResultWithEvent
from domain.repositories.twich.stream_repository import TwichStreamRepository
from infrastructure.connections.mongo.database import MongoDatabase
from infrastructure.mappers.twich.mongo.stream_mapper import TwichStreamMapper
from infrastructure.models.twich.mongo.stream_model import TwichStream


class TwichStreamMongoRepository(TwichStreamRepository):
    """
    TwichStreamMongoRepository: Mongo implementation of TwichStreamRepository.

    Args:
        TwichStreamRepository (_type_): Repository abstract class.
    """

    def __init__(self, db: MongoDatabase) -> None:
        """
        __init__: Initialize repository.

        Args:
            db (MongoDatabase): MongoDatabase instance, containing mongo connection.
        """

        self.db = db

    def parse_stream(self, user_login: str) -> PublicParseStreamCalledEvent:
        """
        parse_stream: Return event about parsing twich stream.

        Args:
            user_login (str): Login of the user.

        Returns:
            PublicParseStreamCalledEvent: Event about parsing stream.
        """

        return PublicParseStreamCalledEvent(type='twich_stream', user_login=user_login)

    def create_or_update(
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
            tags=stream_persistence.tags,
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

    def all(self) -> list[TwichStreamEntity]:
        """
        all: Return list of twich streams.

        Returns:
            list[TwichStreamEntity]: List of twich streams.
        """

        return [
            TwichStreamMapper.to_domain(stream_persistence)
            for stream_persistence in TwichStream.objects
        ]

    def delete_stream_by_user_login(self, user_login: str) -> TwichStreamDeletedByUserLoginEvent:
        """
        delete_stream_by_user_login: Delete stream by user login.

        Args:
            user_login (str): Login of the user.

        Returns:
            TwichStreamDeletedByUserLoginEvent: Twich stream deleted event.
        """

        for stream_persistence in TwichStream.objects(user_login=user_login):
            stream_persistence.delete()

        return TwichStreamDeletedByUserLoginEvent(user_login=user_login)

    def get_stream_by_user_login(self, user_login: str) -> TwichStreamEntity:
        """
        get_stream_by_user_login: Return stream by user login.

        Args:
            user_login (str): Login of the user.

        Returns:
            TwichStreamEntity: Twich stream entity.
        """

        stream_persistence: Optional[TwichStream] = TwichStream.objects(
            user_login=user_login,
        ).first()

        if not stream_persistence:
            raise StreamNotFoundException

        return TwichStreamMapper.to_domain(stream_persistence)
