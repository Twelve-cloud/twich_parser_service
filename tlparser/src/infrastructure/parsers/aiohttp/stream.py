"""
stream.py: File, containing domain service for a twich stream.
"""


from datetime import datetime
from typing import Optional
from aiohttp import ClientSession
from common.config.twich.settings import settings
from domain.dependencies.token import TwichAPIToken
from domain.exceptions.common import TwichRequestUnauthorizedException
from domain.exceptions.stream import GetStreamBadRequestException, StreamNotFoundException
from domain.models.stream import TwichStream


class TwichStreamDomainService:
    """
    TwichStreamDomainService: Class, that contains parsing logic for a twich stream.
    It parse twich stream from Twich, then create it and return.
    """

    def __init__(self, token: TwichAPIToken) -> None:
        """
        __init__: Initialize twich stream domain service class instance.

        Args:
            token (TwichAPIToken): Token for Twich API.
        """

        self.token: TwichAPIToken = token

    async def parse_stream(self, user_login: str) -> TwichStream:
        """
        parse_stream: Parse stream data from the Twich, then create it and return.

        Args:
            user_login (str): Login of the user.

        Raises:
            GetStreamBadRequestException: Raised when request to Twich API return 400 status code.
            GetStreamUnauthorizedException: Raised when request to Twich API return 401 status code.
            StreamNotFoundException: Raised when request to Twich API does not return a stream.

        Returns:
            TwichStream: Twich stream domain model instance.
        """

        async with ClientSession() as session:
            async with session.get(
                f'{settings.TWICH_GET_STREAM_BASE_URL}?user_login={user_login}',
                headers=self.token.headers,
                timeout=10,
            ) as response:
                if response.status == 400:
                    raise GetStreamBadRequestException

                if response.status == 401:
                    raise TwichRequestUnauthorizedException

                stream_json: Optional[dict] = await response.json()

                if not stream_json:
                    raise StreamNotFoundException

                stream_data: Optional[list] = stream_json.get('data')

                if not stream_data:
                    raise StreamNotFoundException

                stream: TwichStream = TwichStream.create(
                    **stream_data[0],
                    parsed_at=datetime.utcnow(),
                )
                stream.started_at = datetime.strptime(
                    stream_data[0]['started_at'],
                    '%Y-%m-%dT%H:%M:%SZ',
                )

                return stream
