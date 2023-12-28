"""
user_repository.py: File, containing twich user mongo repository implementation.
"""


from typing import Optional
from domain.entities.twich.user_entity import TwichUserEntity
from domain.events.twich.user_events import (
    PublicParseUserCalledEvent,
    TwichUserCreatedOrUpdatedEvent,
    TwichUserDeletedByLoginEvent,
)
from domain.exceptions.twich.user_exceptions import UserNotFoundException
from domain.interfaces.repositories.twich.user_repository import ITwichUserRepository
from domain.types.types import ResultWithEvent
from infrastructure.connections.mongo.database import MongoDatabase
from infrastructure.mappers.twich.mongo.user_mapper import TwichUserMapper
from infrastructure.models.twich.mongo.user_model import TwichUser


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

    async def parse_user(self, login: str) -> PublicParseUserCalledEvent:
        """
        parse_user: Return event about parsing twich user.

        Args:
            login (str): Login of the user.

        Returns:
            PublicParseUserCalledEvent: Event about parsing user.
        """

        return PublicParseUserCalledEvent(type='twich_user', login=login)

    async def create_or_update(
        self, user_entity: TwichUserEntity
    ) -> ResultWithEvent[TwichUserEntity, TwichUserCreatedOrUpdatedEvent]:
        """
        create_or_update: Create or update twich user.

        Args:
            user_entity (TwichUserEntity): Twich user entity.

        Returns:
            ResultWithEvent[Result, Event]:: Created/Updated twich user entity.
        """

        user_persistence = TwichUserMapper.to_persistence(user_entity)
        user_persistence.save()

        event: TwichUserCreatedOrUpdatedEvent = TwichUserCreatedOrUpdatedEvent(
            id=user_persistence.id,
            login=user_persistence.login,
            description=user_persistence.description,
            display_name=user_persistence.display_name,
            type=user_persistence.type,
            broadcaster_type=user_persistence.broadcaster_type,
            profile_image_url=user_persistence.profile_image_url,
            offline_image_url=user_persistence.offline_image_url,
            created_at=user_persistence.created_at,
            parsed_at=user_persistence.parsed_at,
        )
        entity: TwichUserEntity = TwichUserMapper.to_domain(user_persistence)

        return ResultWithEvent[TwichUserEntity, TwichUserCreatedOrUpdatedEvent](
            result=entity,
            event=event,
        )

    async def all(self) -> list[TwichUserEntity]:
        """
        all: Return list of twich users.

        Returns:
            list[TwichUserEntity]: List of twich users.
        """

        return [
            TwichUserMapper.to_domain(user_persistence) for user_persistence in TwichUser.objects
        ]

    async def delete_user_by_login(self, login: str) -> TwichUserDeletedByLoginEvent:
        """
        delete_user_by_login: Delete user by login.

        Args:
            user_login (str): Login of the user.

        Returns:
            TwichUserDeletedByLoginEvent: Twich user deleted event.
        """

        for user_persistence in TwichUser.objects(login=login):
            user_persistence.delete()

        return TwichUserDeletedByLoginEvent(login=login)

    async def get_user_by_login(self, login: str) -> TwichUserEntity:
        """
        get_user_by_login: Return user by login.

        Args:
            user_login (str): Login of the user.

        Returns:
            TwichUserEntity: Twich user entity.
        """

        user_persistence: Optional[TwichUser] = TwichUser.objects(login=login).first()

        if not user_persistence:
            raise UserNotFoundException

        return TwichUserMapper.to_domain(user_persistence)
