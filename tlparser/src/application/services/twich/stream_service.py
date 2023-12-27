"""
stream_service.py: File, containing service for a twich stream.
"""


from fastapi import status
from requests import Response, get
from application.dependencies.twich.token_dependency import TwichAPIToken
from common.config.twich.settings import settings
from domain.entities.twich.stream_entity import TwichStreamEntity
from domain.events.twich.stream_events import (
    PublicParseStreamCalledEvent,
    TwichStreamCreatedOrUpdatedEvent,
    TwichStreamDeletedByUserLoginEvent,
)
from domain.exceptions.twich.stream_exceptions import (
    GetStreamBadRequestException,
    GetStreamUnauthorizedException,
    StreamNotFoundException,
)
from domain.publishers.twich.stream_publisher import ITwichStreamPublisher
from domain.repositories.base.base_repository import ResultWithEvent
from domain.repositories.twich.stream_repository import ITwichStreamRepository


class TwichStreamService:
    """
    TwichStreamService: Class, that contains business logic for twich streams.
    """

    def __init__(
        self,
        repository: ITwichStreamRepository,
        publisher: ITwichStreamPublisher,
        token: TwichAPIToken,
    ) -> None:
        """
        __init__: Do some initialization for TwichStreamService class.

        Args:
            repository (ITwichStreamRepository): Twich stream repository.
        """

        self.repository: ITwichStreamRepository = repository
        self.publisher: ITwichStreamPublisher = publisher
        self.access_token: str = token.access_token
        self.headers: dict[str, str] = token.headers

    async def parse_stream(self, user_login: str) -> None:
        """
        parse_stream: Called twich stream publisher to publish event about parsing.

        Args:
            user_login (str): Login of the user.
        """

        event: PublicParseStreamCalledEvent = self.repository.parse_stream(user_login)

        self.publisher.publish_parse_stream_called_event(event)

        return

    async def private_parse_stream(self, user_login: str) -> TwichStreamEntity:
        """
        private_parse_stream: Parse stream data from the Twich.

        Args:
            user_login (str): Login of the user.

        Raises:
            GetStreamBadRequestException: Raised when TwichAPI return 400 status code.
            GetStreamUnauthorizedException: Raised when TwichAPI return 401 status code.
            StreamNotFoundException: Raised when TwichAPI return no stream.

        Returns:
            TwichStreamEntity: TwichStreamEntity instance.
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

        stream_entity: TwichStreamEntity = TwichStreamEntity(**stream_data[0])

        stream: ResultWithEvent[TwichStreamEntity, TwichStreamCreatedOrUpdatedEvent] = (
            self.repository.create_or_update(stream_entity)
        )

        stream_event: TwichStreamCreatedOrUpdatedEvent = stream.event

        self.publisher.publish_created_or_updated_event(stream_event)

        return stream.result

    async def delete_stream_by_user_login(self, user_login: str) -> None:
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

    async def get_all_streams(self) -> list[TwichStreamEntity]:
        """
        get_all_streams: Return all twich streams.

        Returns:
            list[TwichStreamEntity]: List of twich streams.
        """

        return self.repository.all()

    async def get_stream_by_user_login(self, user_login: str) -> TwichStreamEntity:
        """
        get_stream_by_user_login _summary_

        Args:
            user_login (str): _description_

        Returns:
            TwichStreamEntity: TwichStreamEntity instance.
        """

        stream_entity: TwichStreamEntity = self.repository.get_stream_by_user_login(user_login)

        return stream_entity
