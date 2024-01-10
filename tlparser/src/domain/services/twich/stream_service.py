"""
stream_service.py: File, containing domain service for a twich stream.
"""


from datetime import datetime
from typing import Optional
from aiohttp import ClientSession
from fastapi import status
from common.config.twich.settings import settings
from domain.dependencies.twich.token_dependency import TwichAPIToken
from domain.entities.twich.stream_entity import TwichStreamEntity
from domain.exceptions.twich.stream_exceptions import (
    GetStreamBadRequestException,
    GetStreamUnauthorizedException,
    StreamNotFoundException,
)


class TwichStreamDomainService:
    """
    TwichStreamDomainService: Class, that contains business logic for twich streams.
    """

    def __init__(self, token: TwichAPIToken) -> None:
        """
        __init__: Do some initialization for TwichStreamDomainService class.

        Args:
            token (TwichAPIToken): Token for twich api.
        """

        self.access_token: str = token.access_token
        self.headers: dict[str, str] = token.headers

    async def parse_stream(self, user_login: str) -> TwichStreamEntity:
        """
        parse_stream: Parse stream data from the Twich.

        Args:
            user_login (str): Login of the user.

        Raises:
            GetStreamBadRequestException: Raised when TwichAPI return 400 status code.
            GetStreamUnauthorizedException: Raised when TwichAPI return 401 status code.
            StreamNotFoundException: Raised when TwichAPI return no stream.

        Returns:
            TwichStreamEntity: TwichStreamEntity instance.
        """

        async with ClientSession() as session:
            async with session.get(
                f'{settings.TWICH_GET_STREAM_BASE_URL}?user_login={user_login}',
                headers=self.headers,
            ) as response:
                if response.status == status.HTTP_400_BAD_REQUEST:
                    raise GetStreamBadRequestException

                if response.status == status.HTTP_401_UNAUTHORIZED:
                    raise GetStreamUnauthorizedException

                stream_data: Optional[dict] = await response.json()

                if not stream_data:
                    raise StreamNotFoundException

                stream: Optional[list] = stream_data.get('data')

                if not stream:
                    raise StreamNotFoundException

                stream_entity: TwichStreamEntity = TwichStreamEntity(**stream[0])
                stream_entity.started_at = datetime.strptime(
                    stream[0]['started_at'],
                    '%Y-%m-%dT%H:%M:%SZ',
                )

                return stream_entity
