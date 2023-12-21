"""
user_service.py: File, containing service for a twich user.
"""


from fastapi import status
from requests import Response, get
from application.dependencies.twich.token_dependency import TwichAPIToken
from application.exceptions.twich.user_exceptions import (
    GetUserBadRequestException,
    GetUserUnauthorizedException,
    UserNotFoundException,
)
from application.mappers.twich.user_mapper import TwichUserCreateMapper, TwichUserReadMapper
from application.schemas.twich.user_schema import TwichUserCreateSchema, TwichUserReadSchema
from common.config.twich.settings import settings
from domain.entities.twich.user_entity import TwichUserEntity
from domain.repositories.twich.user_repository import TwichUserRepository


class TwichUserService:
    """
    TwichUserService: Class, that contains business logic for twich users.
    """

    def __init__(self, repository: TwichUserRepository, token: TwichAPIToken) -> None:
        """
        __init__: Do some initialization for TwichUserService class.

        Args:
            repository (TwichUserRepository): Twich user repository.
        """

        self.repository = repository
        self.access_token = token.access_token
        self.headers = token.headers

    def parse_user(self, user_login: str) -> TwichUserReadSchema:
        """
        parse_user: Parse user data from the Twich.

        Args:
            user_login (str): Login of the user.

        Raises:
            GetUserBadRequestException: Raised when TwichAPI return 400 status code.
            GetUserUnauthorizedException: Raised when TwichAPI return 401 status code.
            UserNotFoundException: Raised when TwichAPI return no user.

        Returns:
            TwichUserReadSchema: TwichUserReadSchema instance.
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

        user_schema: TwichUserCreateSchema = TwichUserCreateSchema(**user_data[0])

        user_entity: TwichUserEntity = self.repository.create_or_update(
            TwichUserCreateMapper.to_domain(user_schema),
        )

        return TwichUserReadMapper.to_schema(user_entity)

    def delete_user_by_login(self, user_login: str) -> None:
        """
        delete_user_by_login: Delete twich user.

        Args:
            user_login (str): Login of the user.
        """

        self.repository.delete_user_by_login(user_login)

        return

    def get_all_users(self) -> list[TwichUserReadSchema]:
        """
        get_all_users: Return list of twich users.

        Returns:
            list[TwichUserReadSchema]: List of twich users.
        """

        return [TwichUserReadMapper.to_schema(user_entity) for user_entity in self.repository.all()]

    def get_user_by_login(self, user_login: str) -> TwichUserReadSchema:
        """
        get_user_by_login: Return user by login.

        Args:
            user_login (str): Login of the user.

        Returns:
            TwichUserReadSchema: TwichUserReadSchema instance.
        """

        user_entity: TwichUserEntity = self.repository.get_user_by_login(user_login)

        return TwichUserReadMapper.to_schema(user_entity)
