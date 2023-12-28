"""
user_service.py: File, containing service for a twich user.
"""


from application.mappers.twich.user_mapper import TwichUserMapper
from application.schemas.twich.user_schema import TwichUserSchema
from domain.entities.twich.user_entity import TwichUserEntity
from domain.events.twich.user_events import (
    PublicParseUserCalledEvent,
    TwichUserCreatedOrUpdatedEvent,
    TwichUserDeletedByLoginEvent,
)
from domain.interfaces.publishers.twich.user_publisher import ITwichUserPublisher
from domain.interfaces.repositories.twich.user_repository import ITwichUserRepository
from domain.services.twich.user_service import TwichUserDomainService
from domain.types.types import ResultWithEvent


class TwichUserRestService:
    """
    TwichUserRestService: Class, that contains business logic for twich users.
    """

    def __init__(
        self,
        domain_service: TwichUserDomainService,
        publisher: ITwichUserPublisher,
        repository: ITwichUserRepository,
    ) -> None:
        """
        __init__: Do some initialization for TwichUserRestService class.

        Args:
            domain_service (TwichUserDomainService): Twich user domain service.
            publisher (ITwichUserPublisher): Twich user publisher.
            repository (ITwichUserRepository): Twich user repository.
        """

        self.domain_service: TwichUserDomainService = domain_service
        self.publisher: ITwichUserPublisher = publisher
        self.repository: ITwichUserRepository = repository

    async def parse_user(self, user_login: str) -> None:
        """
        parse_user: Called twich user publisher to publish event about parsing.

        Args:
            user_login (str): Login of the user.
        """

        event: PublicParseUserCalledEvent = await self.repository.parse_user(user_login)

        await self.publisher.publish_parse_user_called_event(event)

        return

    async def private_parse_user(self, user_login: str) -> TwichUserSchema:
        """
        private_parse_user: Parse user data from the Twich.

        Args:
            user_login (str): Login of the user.

        Returns:
            TwichUserEntity: TwichUserSchema instance.
        """

        user_entity: TwichUserEntity = await self.domain_service.parse_user(user_login)

        user: ResultWithEvent[TwichUserEntity, TwichUserCreatedOrUpdatedEvent] = (
            await self.repository.create_or_update(user_entity)
        )

        user_event: TwichUserCreatedOrUpdatedEvent = user.event

        await self.publisher.publish_created_or_updated_event(user_event)

        return TwichUserMapper.to_schema(user.result)

    async def create(self, schema: TwichUserSchema) -> None:
        """
        create: Create twich user.

        Args:
            schema (TwichUserSchema): Twich user schema.
        """

        await self.repository.create_or_update(TwichUserMapper.to_domain(schema))

    async def delete_user_by_login(self, user_login: str) -> None:
        """
        delete_user_by_login: Delete twich user.

        Args:
            user_login (str): Login of the user.
        """

        event: TwichUserDeletedByLoginEvent = await self.repository.delete_user_by_login(user_login)

        await self.publisher.publish_user_deleted_by_login_event(event)

        return

    async def get_all_users(self) -> list[TwichUserSchema]:
        """
        get_all_users: Return list of twich users.

        Returns:
            list[TwichUserSchema]: List of twich users.
        """

        return [
            TwichUserMapper.to_schema(user_entity) for user_entity in await self.repository.all()
        ]

    async def get_user_by_login(self, user_login: str) -> TwichUserSchema:
        """
        get_user_by_login: Return user by login.

        Args:
            user_login (str): Login of the user.

        Returns:
            TwichUserSchema: TwichUserSchema instance.
        """

        user_entity: TwichUserEntity = await self.repository.get_user_by_login(user_login)

        return TwichUserMapper.to_schema(user_entity)
