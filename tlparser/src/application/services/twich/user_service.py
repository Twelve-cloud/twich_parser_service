"""
user_service.py: File, containing service for a twich user.
"""


from fastapi import status
from requests import Response, get
from application.dependencies.twich.token_dependency import TwichAPIToken
from common.config.twich.settings import settings
from domain.entities.twich.user_entity import TwichUserEntity
from domain.events.twich.user_events import (
    PublicParseUserCalledEvent,
    TwichUserCreatedOrUpdatedEvent,
    TwichUserDeletedByLoginEvent,
)
from domain.exceptions.twich.user_exceptions import (
    GetUserBadRequestException,
    GetUserUnauthorizedException,
    UserNotFoundException,
)
from domain.publishers.twich.user_publisher import ITwichUserPublisher
from domain.repositories.base.base_repository import ResultWithEvent
from domain.repositories.twich.user_repository import ITwichUserRepository


class TwichUserService:
    """
    TwichUserService: Class, that contains business logic for twich users.
    """

    def __init__(
        self,
        repository: ITwichUserRepository,
        publisher: ITwichUserPublisher,
        token: TwichAPIToken,
    ) -> None:
        """
        __init__: Do some initialization for TwichUserService class.

        Args:
            repository (ITwichUserRepository): Twich user repository.
        """

        self.repository: ITwichUserRepository = repository
        self.publisher: ITwichUserPublisher = publisher
        self.access_token: str = token.access_token
        self.headers: dict[str, str] = token.headers

    async def parse_user(self, user_login: str) -> None:
        """
        parse_user: Called twich user publisher to publish event about parsing.

        Args:
            user_login (str): Login of the user.
        """

        event: PublicParseUserCalledEvent = self.repository.parse_user(user_login)

        self.publisher.publish_parse_user_called_event(event)

        return

    async def private_parse_user(self, user_login: str) -> TwichUserEntity:
        """
        private_parse_user: Parse user data from the Twich.

        Args:
            user_login (str): Login of the user.

        Raises:
            GetUserBadRequestException: Raised when TwichAPI return 400 status code.
            GetUserUnauthorizedException: Raised when TwichAPI return 401 status code.
            UserNotFoundException: Raised when TwichAPI return no user.

        Returns:
            TwichUserEntity: TwichUserEntity instance.
        """

        response: Response = get(
            f'{settings.TWICH_GET_USER_BASE_URL}?login={user_login}',
            headers=self.headers,
        )

        if response.status_code == status.HTTP_400_BAD_REQUEST:
            raise GetUserBadRequestException

        if response.status_code == status.HTTP_401_UNAUTHORIZED:
            raise GetUserUnauthorizedException

        user_data: list = response.json().get('data')

        if not user_data:
            raise UserNotFoundException

        user_entity: TwichUserEntity = TwichUserEntity(**user_data[0])

        user: ResultWithEvent[TwichUserEntity, TwichUserCreatedOrUpdatedEvent] = (
            self.repository.create_or_update(user_entity)
        )

        user_event: TwichUserCreatedOrUpdatedEvent = user.event

        self.publisher.publish_created_or_updated_event(user_event)

        return user.result

    async def delete_user_by_login(self, user_login: str) -> None:
        """
        delete_user_by_login: Delete twich user.

        Args:
            user_login (str): Login of the user.
        """

        event: TwichUserDeletedByLoginEvent = self.repository.delete_user_by_login(user_login)

        self.publisher.publish_user_deleted_by_login_event(event)

        return

    async def get_all_users(self) -> list[TwichUserEntity]:
        """
        get_all_users: Return list of twich users.

        Returns:
            list[TwichUserEntity]: List of twich users.
        """

        return self.repository.all()

    async def get_user_by_login(self, user_login: str) -> TwichUserEntity:
        """
        get_user_by_login: Return user by login.

        Args:
            user_login (str): Login of the user.

        Returns:
            TwichUserEntity: TwichUserEntity instance.
        """

        user_entity: TwichUserEntity = self.repository.get_user_by_login(user_login)

        return user_entity
