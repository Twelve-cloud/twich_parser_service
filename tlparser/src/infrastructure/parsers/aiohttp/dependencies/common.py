"""
common.py: File, containing common dependencies.
"""


from typing import AsyncGenerator
from aiohttp import ClientSession
from common.config import settings
from domain.exceptions import TwichTokenNotObtainedException


class TwichAPIToken:
    """
    TwichAPIToken: Class, that represents Twich API token.
    """

    def __init__(self, access_token: str) -> None:
        """
        __init__: Initialize Twich API token class instance.

        Args:
            access_token (str): Acccess token for Twich API.
        """

        self._access_token: str = access_token

    @property
    def headers(self) -> dict[str, str]:
        """
        headers: Return headers for any request to Twich API.

        Returns:
            dict[str, str]: Dict where key is header name and value is header value.
        """

        return {
            'Authorization': f'{settings.TWICH_API_TOKEN_TYPE} {self._access_token}',
            'Client-Id': settings.TWICH_CLIENT_ID,
        }


async def get_twich_api_token() -> AsyncGenerator[TwichAPIToken, None]:
    """
    get_twich_api_token: Make request to Twich API to obtain Twich API token.

    Yields:
        TwichAPIToken: Twich API token instance.
    """

    async with ClientSession() as session:
        async with session.post(
            settings.TWICH_TOKEN_URL,
            headers={
                'Content-Type': settings.TWICH_API_CONTENT_TYPE,
            },
            json={
                'client_id': settings.TWICH_CLIENT_ID,
                'client_secret': settings.TWICH_CLIENT_SECRET,
                'grant_type': settings.TWICH_API_GRANT_TYPE,
            },
        ) as response:
            try:
                json_response: dict = await response.json()
                access_token: str = json_response['access_token']
                yield TwichAPIToken(access_token)
            except Exception as exception:
                raise TwichTokenNotObtainedException(f'Error during obtaining token: {exception}')
