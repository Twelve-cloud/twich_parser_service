"""
user.py: File, containing parser for a twich user.
"""


from datetime import datetime
from typing import Optional
from aiohttp import ClientSession
from common.config import settings
from domain.exceptions import (
    ObjectNotFoundException,
    TwichGetObjectBadRequestException,
    TwichRequestUnauthorizedException,
)
from domain.models import TwichUser
from infrastructure.parsers.dependencies import TwichAPIToken


class TwichUserParser:
    """
    TwichUserParser: Class, that contains parsing logic for a twich user.
    It parse twich user from Twich, then create it and return.
    """

    def __init__(self, token: TwichAPIToken) -> None:
        """
        __init__: Initialize twich user parser class instance.

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
            TwichGetObjectBadRequestException: Raised when request to Twich API return 400 code.
            GetGameUnauthorizedException: Raised when request to Twich API return 401 code.
            ObjectNotFoundException: Raised when request to Twich API does not return a stream.

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
                    raise TwichGetObjectBadRequestException('Get user bad request to Twich API.')

                if response.status == 401:
                    raise TwichRequestUnauthorizedException('Request to Twich API is unauthorized.')

                user_json: Optional[dict] = await response.json()

                if not user_json:
                    raise ObjectNotFoundException('User is not found.')

                user_data: Optional[list] = user_json.get('data')

                if not user_data:
                    raise ObjectNotFoundException('User is not found.')

                user: TwichUser = TwichUser.create(
                    **user_data[0],
                    parsed_at=datetime.utcnow(),
                )
                user.created_at = datetime.strptime(
                    user_data[0]['created_at'],
                    '%Y-%m-%dT%H:%M:%SZ',
                )

                return user
