"""
user_service.py: File, containing domain service for a twich user.
"""


from datetime import datetime
from typing import Optional
from aiohttp import ClientSession
from fastapi import status
from common.config.twich.settings import settings
from domain.dependencies.twich.token_dependency import TwichAPIToken
from domain.entities.twich.user_entity import TwichUserEntity
from domain.exceptions.twich.user_exceptions import (
    GetUserBadRequestException,
    GetUserUnauthorizedException,
    UserNotFoundException,
)


class TwichUserDomainService:
    """
    TwichUserDomainService: Class, that contains business logic for twich users.
    """

    def __init__(self, token: TwichAPIToken) -> None:
        """
        __init__: Do some initialization for TwichUserDomainService class.

        Args:
            token (TwichAPIToken): Token for twich api.
        """

        self.access_token: str = token.access_token
        self.headers: dict[str, str] = token.headers

    async def parse_user(self, user_login: str) -> TwichUserEntity:
        """
        parse_user: Parse user data from the Twich.

        Args:
            user_login (str): Login of the user.

        Raises:
            GetUserBadRequestException: Raised when TwichAPI return 400 status code.
            GetUserUnauthorizedException: Raised when TwichAPI return 401 status code.
            UserNotFoundException: Raised when TwichAPI return no user.

        Returns:
            TwichUserEntity: TwichUserEntity instance.
        """

        async with ClientSession() as session:
            async with session.get(
                f'{settings.TWICH_GET_USER_BASE_URL}?login={user_login}',
                headers=self.headers,
            ) as response:
                if response.status == status.HTTP_400_BAD_REQUEST:
                    raise GetUserBadRequestException

                if response.status == status.HTTP_401_UNAUTHORIZED:
                    raise GetUserUnauthorizedException

                user_data: Optional[dict] = await response.json()

                if not user_data:
                    raise UserNotFoundException

                user: Optional[list] = user_data.get('data')

                if not user:
                    raise UserNotFoundException

                user_entity: TwichUserEntity = TwichUserEntity(**user[0])
                user_entity.created_at = datetime.strptime(
                    user[0]['created_at'],
                    '%Y-%m-%dT%H:%M:%SZ',
                )

                return user_entity
