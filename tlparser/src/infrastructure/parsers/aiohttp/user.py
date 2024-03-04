"""
user.py: File, containing domain service for a twich user.
"""


from datetime import datetime
from typing import Optional
from aiohttp import ClientSession
from common.config.twich.settings import settings
from domain.dependencies.token import TwichAPIToken
from domain.exceptions.common import TwichRequestUnauthorizedException
from domain.exceptions.user import GetUserBadRequestException, UserNotFoundException
from domain.models.user import TwichUser


class TwichUserDomainService:
    """
    TwichUserDomainService: Class, that contains parsing logic for a twich user.
    It parse twich user from Twich, then create it and return.
    """

    def __init__(self, token: TwichAPIToken) -> None:
        """
        __init__: Initialize twich user domain service class instance.

        Args:
            token (TwichAPIToken): Token for Twich API.
        """

        self.token: TwichAPIToken = token

    async def parse_user(self, login: str) -> TwichUser:
        """
        parse_user: Parse user data from the Twich, then create it and return.

        Args:
            login (str): Login of the user.

        Raises:
            GetUserBadRequestException: Raised when request to Twich API return 400 status code.
            GetUserUnauthorizedException: Raised when request to Twich API return 401 status code.
            UserNotFoundException: Raised when request to Twich API does not return a user.

        Returns:
            TwichUser: Twich user domain model instance.
        """

        async with ClientSession() as session:
            async with session.get(
                f'{settings.TWICH_GET_USER_BASE_URL}?login={login}',
                headers=self.token.headers,
                timeout=10,
            ) as response:
                if response.status == 400:
                    raise GetUserBadRequestException

                if response.status == 401:
                    raise TwichRequestUnauthorizedException

                user_json: Optional[dict] = await response.json()

                if not user_json:
                    raise UserNotFoundException

                user_data: Optional[list] = user_json.get('data')

                if not user_data:
                    raise UserNotFoundException

                user: TwichUser = TwichUser.create(
                    **user_data[0],
                    parsed_at=datetime.utcnow(),
                )
                user.created_at = datetime.strptime(
                    user_data[0]['created_at'],
                    '%Y-%m-%dT%H:%M:%SZ',
                )

                return user
