"""
user.py: File, containing parser for a twich user.
"""


from datetime import datetime
from typing import Optional
from aiohttp import ClientSession
from common.config import settings
from application.exceptions import (
    ObjectNotFoundException,
    TwichGetObjectBadRequestException,
    TwichRequestUnauthorizedException,
)
from domain.models import TwichUser
from infrastructure.parsers.aiohttp.dependencies import TwichAPIToken


class TwichUserParser:
    def __init__(self, token: TwichAPIToken) -> None:
        self.token: TwichAPIToken = token

    async def parse_user(self, login: str) -> TwichUser:
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
