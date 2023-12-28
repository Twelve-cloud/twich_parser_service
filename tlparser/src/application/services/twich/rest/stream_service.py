"""
stream_service.py: File, containing service for a twich stream.
"""


from application.mappers.twich.stream_mapper import TwichStreamMapper
from application.schemas.twich.stream_schema import TwichStreamSchema
from domain.entities.twich.stream_entity import TwichStreamEntity
from domain.events.twich.stream_events import (
    PublicParseStreamCalledEvent,
    TwichStreamCreatedOrUpdatedEvent,
    TwichStreamDeletedByUserLoginEvent,
)
from domain.interfaces.publishers.twich.stream_publisher import ITwichStreamPublisher
from domain.interfaces.repositories.twich.stream_repository import ITwichStreamRepository
from domain.services.twich.stream_service import TwichStreamDomainService
from domain.types.types import ResultWithEvent


class TwichStreamRestService:
    """
    TwichStreamRestService: Class, that contains business logic for twich streams.
    """

    def __init__(
        self,
        domain_service: TwichStreamDomainService,
        publisher: ITwichStreamPublisher,
        repository: ITwichStreamRepository,
    ) -> None:
        """
        __init__: Do some initialization for TwichStreamRestService class.

        Args:
            domain_service (TwichStreamDomainService): Twich stream domain service.
            publisher (ITwichStreamPublisher): Twich stream publisher.
            repository (ITwichStreamRepository): Twich stream repository.
        """

        self.domain_service: TwichStreamDomainService = domain_service
        self.publisher: ITwichStreamPublisher = publisher
        self.repository: ITwichStreamRepository = repository

    async def parse_stream(self, user_login: str) -> None:
        """
        parse_stream: Called twich stream publisher to publish event about parsing.

        Args:
            user_login (str): Login of the user.
        """

        event: PublicParseStreamCalledEvent = await self.repository.parse_stream(user_login)

        await self.publisher.publish_parse_stream_called_event(event)

        return

    async def private_parse_stream(self, user_login: str) -> TwichStreamSchema:
        """
        private_parse_stream: Parse stream data from the Twich.

        Args:
            user_login (str): Login of the user.

        Returns:
            TwichStreamSchema: TwichStreamSchema instance.
        """

        stream_entity: TwichStreamEntity = await self.domain_service.parse_stream(user_login)

        stream: ResultWithEvent[TwichStreamEntity, TwichStreamCreatedOrUpdatedEvent] = (
            await self.repository.create_or_update(stream_entity)
        )

        stream_event: TwichStreamCreatedOrUpdatedEvent = stream.event

        await self.publisher.publish_created_or_updated_event(stream_event)

        return TwichStreamMapper.to_schema(stream.result)

    async def create(self, schema: TwichStreamSchema) -> None:
        """
        create: Create twich stream.

        Args:
            schema (TwichStreamSchema): Twich stream schema.
        """

        await self.repository.create_or_update(TwichStreamMapper.to_domain(schema))

    async def delete_stream_by_user_login(self, user_login: str) -> None:
        """
        delete_stream_by_user_login: Delete twich stream.

        Args:
            user_login (str): Login of the user.
        """

        event: TwichStreamDeletedByUserLoginEvent = (
            await self.repository.delete_stream_by_user_login(user_login)
        )

        await self.publisher.publish_stream_deleted_by_user_login_event(event)

        return

    async def get_all_streams(self) -> list[TwichStreamSchema]:
        """
        get_all_streams: Return all twich streams.

        Returns:
            list[TwichStreamSchema]: List of twich streams.
        """

        return [
            TwichStreamMapper.to_schema(stream_entity)
            for stream_entity in await self.repository.all()
        ]

    async def get_stream_by_user_login(self, user_login: str) -> TwichStreamSchema:
        """
        get_stream_by_user_login _summary_

        Args:
            user_login (str): _description_

        Returns:
            TwichStreamSchema: TwichStreamSchema instance.
        """

        stream_entity: TwichStreamEntity = await self.repository.get_stream_by_user_login(
            user_login,
        )

        return TwichStreamMapper.to_schema(stream_entity)
