"""
stream.py: File, containing parser for a twich stream.
"""


from datetime import datetime
from typing import Optional

from aiohttp import ClientSession

from application.exceptions import (
    ObjectNotFoundException,
    TwichGetObjectBadRequestException,
    TwichRequestUnauthorizedException,
)
from domain.models import TwichStream
from infrastructure.parsers.aiohttp.dependencies import TwichAPIToken
from shared.config import settings


class TwichStreamParser:
    def __init__(self, token: TwichAPIToken) -> None:
        self.token: TwichAPIToken = token

    async def parse_stream(self, user_login: str) -> TwichStream:
        async with ClientSession() as session:
            async with session.get(
                f'{settings.TWICH_GET_STREAM_BASE_URL}?user_login={user_login}',
                headers=self.token.headers,
                timeout=10,
            ) as response:
                if response.status == 400:
                    raise TwichGetObjectBadRequestException('Get stream bad request to Twich API.')

                if response.status == 401:
                    raise TwichRequestUnauthorizedException('Request to Twich API is unauthorized.')

                stream_json: Optional[dict] = await response.json()

                if not stream_json:
                    raise ObjectNotFoundException('Stream is not found.')

                stream_data: Optional[list] = stream_json.get('data')

                if not stream_data:
                    raise ObjectNotFoundException('Stream is not found.')

                stream: TwichStream = TwichStream.create(
                    **stream_data[0],
                    parsed_at=datetime.utcnow(),
                )
                stream.started_at = datetime.strptime(
                    stream_data[0]['started_at'],
                    '%Y-%m-%dT%H:%M:%SZ',
                )

                return stream
