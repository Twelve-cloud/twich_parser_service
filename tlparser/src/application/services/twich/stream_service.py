"""
stream_service.py: File, containing service for a twich stream.
"""


from fastapi import status
from requests import Response, get
from application.dependencies.twich.token_dependency import TwichAPIToken
from application.exceptions.twich.stream_exceptions import (
    GetStreamBadRequestException,
    GetStreamUnauthorizedException,
    StreamNotFoundException,
)
from application.mappers.twich.stream_mapper import TwichStreamCreateMapper, TwichStreamReadMapper
from application.schemas.twich.stream_schema import TwichStreamCreateSchema, TwichStreamReadSchema
from common.config.twich.settings import settings
from domain.entities.twich.stream_entity import TwichStreamEntity
from domain.events.twich.stream_events import (
    PublicParseStreamCalledEvent,
    TwichStreamCreatedOrUpdatedEvent,
    TwichStreamDeletedByUserLoginEvent,
)
from domain.publishers.twich.stream_publisher import TwichStreamPublisher
from domain.repositories.base.base_repository import ResultWithEvent
from domain.repositories.twich.stream_repository import TwichStreamRepository


class TwichStreamService:
    """
    TwichStreamService: Class, that contains business logic for twich streams.
    """

    def __init__(
        self,
        repository: TwichStreamRepository,
        publisher: TwichStreamPublisher,
        token: TwichAPIToken,
    ) -> None:
        """
        __init__: Do some initialization for TwichStreamService class.

        Args:
            repository (TwichStreamRepository): Twich stream repository.
        """

        self.repository = repository
        self.publisher = publisher
        self.access_token = token.access_token
        self.headers = token.headers

    def parse_stream(self, user_login: str) -> None:
        """
        parse_stream: Called twich stream publisher to publish event about parsing.

        Args:
            user_login (str): Login of the user.
        """

        event: PublicParseStreamCalledEvent = self.repository.parse_stream(user_login)

        self.publisher.publish_parse_stream_called_event(event)

        return

    def private_parse_stream(self, user_login: str) -> TwichStreamReadSchema:
        """
        private_parse_stream: Parse stream data from the Twich.

        Args:
            user_login (str): Login of the user.

        Raises:
            GetStreamBadRequestException: Raised when TwichAPI return 400 status code.
            GetStreamUnauthorizedException: Raised when TwichAPI return 401 status code.
            StreamNotFoundException: Raised when TwichAPI return no stream.

        Returns:
            TwichStreamReadSchema: TwichStreamReadSchema instance.
        """

        response: Response = get(
            f'{settings.TWICH_GET_STREAM_BASE_URL}?user_login={user_login}',
            headers=self.headers,
        )

        if response.status_code == status.HTTP_400_BAD_REQUEST:
            raise GetStreamBadRequestException

        if response.status_code == status.HTTP_401_UNAUTHORIZED:
            raise GetStreamUnauthorizedException

        stream_data: list = response.json().get('data')

        if not stream_data:
            raise StreamNotFoundException

        stream_schema: TwichStreamCreateSchema = TwichStreamCreateSchema(**stream_data[0])

        stream: ResultWithEvent[TwichStreamEntity, TwichStreamCreatedOrUpdatedEvent] = (
            self.repository.create_or_update(
                TwichStreamCreateMapper.to_domain(stream_schema),
            )
        )

        stream_event: TwichStreamCreatedOrUpdatedEvent = stream.event

        self.publisher.publish_created_or_updated_event(stream_event)

        stream_entity: TwichStreamEntity = stream.result

        return TwichStreamReadMapper.to_schema(stream_entity)

    def delete_stream_by_user_login(self, user_login: str) -> None:
        """
        delete_stream_by_user_login: Delete twich stream.

        Args:
            user_login (str): Login of the user.
        """

        event: TwichStreamDeletedByUserLoginEvent = self.repository.delete_stream_by_user_login(
            user_login
        )

        self.publisher.publish_stream_deleted_by_user_login_event(event)

        return

    def get_all_streams(self) -> list[TwichStreamReadSchema]:
        """
        get_all_streams: Return all twich streams.

        Returns:
            list[TwichStreamReadSchema]: List of twich streams.
        """

        return [
            TwichStreamReadMapper.to_schema(stream_entity)
            for stream_entity in self.repository.all()
        ]

    def get_stream_by_user_login(self, user_login: str) -> TwichStreamReadSchema:
        """
        get_stream_by_user_login _summary_

        Args:
            user_login (str): _description_

        Returns:
            TwichStreamReadSchema: TwichStreamReadSchema instance.
        """

        stream_entity: TwichStreamEntity = self.repository.get_stream_by_user_login(user_login)

        return TwichStreamReadMapper.to_schema(stream_entity)
