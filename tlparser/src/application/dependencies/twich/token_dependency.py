"""
token_dependency.py: File, containing token dependency for a twich app.
"""


from requests import Response, post
from common.config.twich.settings import settings


class TwichAPIToken:
    """
    TwichAPIToken: Class, containing twich api token.
    """

    def __init__(self) -> None:
        """
        __init__: Initialize TwichAPIToken class.
        """

        self.access_token = self._get_twich_api_token()
        self.headers = self._prepare_token_headers()

    def _get_twich_api_token(self) -> str:
        """
        _get_twich_api_token: Return access token for TwichAPI.

        Returns:
            access_token: Access token for TwichAPI.
        """

        response: Response = post(
            settings.TWICH_TOKEN_URL,
            headers={
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            data={
                'client_id': settings.TWICH_CLIENT_ID,
                'client_secret': settings.TWICH_CLIENT_SECRET,
                'grant_type': 'client_credentials',
            },
        )

        return response.json().get('access_token')

    def _prepare_token_headers(self) -> dict[str, str]:
        """
        _prepare_token_headers: Return headers for TwichAPI requests.

        Returns:
            dict[str, str]: Dict where key is header name and value is header value.
        """

        return {
            'Authorization': f'Bearer {self.access_token}',
            'Client-Id': settings.TWICH_CLIENT_ID,
        }
