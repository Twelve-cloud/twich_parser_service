"""
twich_services.py: File, containing services for a twich app.
"""


from fastapi import status
from requests import Response, get, post
from config.twich_settings import settings
from schemas.twich_schemas import TwichGameSchema, TwichUserSchema, TwichStreamSchema
from repositories.irepositories import ITwichRepository
from exceptions.twich_exceptions import (
    GameNotFoundException,
    UserNotFoundException,
    StreamNotFoundException,
    GetGameBadRequestException,
    GetUserBadRequestException,
    GetGameUnauthorizedException,
    GetStreamBadRequestException,
    GetUserUnauthorizedException,
    GetStreamUnauthorizedException,
)


class TwichService:
    """
    TwichService: Class, that contains parsing logic for a twich app.
    """

    def __init__(self, twich_repository: ITwichRepository) -> None:
        """
        __init__: Obtain access token for TwichAPI and do some initialization.

        Args:
            twich_repository (ITwichRepository): Twich repository.
        """

        self.repository = twich_repository
        self.access_token: str = self._get_twich_api_token()

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

    def _prepare_headers(self) -> dict[str, str]:
        return {
            'Authorization': f'Bearer {self.access_token}',
            'Client-Id': settings.TWICH_CLIENT_ID,
        }

    def parse_game(self, game_name: str) -> TwichGameSchema:
        """
        parse_game: Parse game data from the Twich.

        Args:
            game_name (str): Name of the game.

        Raises:
            GetGameBadRequestException: Raised when TwichAPI return 400 status code.
            GetGameUnauthorizedException: Raised when TwichAPI return 401 status code.
            GameNotFoundException: Raised when TwichAPI return no game.

        Returns:
            TwichGameSchema: TwichGameSchema instance.
        """

        response: Response = get(
            f'{settings.TWICH_GET_GAME_BASE_URL}?name={game_name}',
            headers=self._prepare_headers(),
        )

        if response.status_code == status.HTTP_400_BAD_REQUEST:
            raise GetGameBadRequestException

        if response.status_code == status.HTTP_401_UNAUTHORIZED:
            raise GetGameUnauthorizedException

        game_data: list = response.json().get('data')

        if not game_data:
            raise GameNotFoundException

        game: TwichGameSchema = TwichGameSchema(**game_data[0])

        # repository actions

        return game

    def parse_user(self, user_login: str) -> TwichUserSchema:
        """
        parse_user: Parse user data from the Twich.

        Args:
            user_login (str): Login of the user.

        Raises:
            GetUserBadRequestException: Raised when TwichAPI return 400 status code.
            GetUserUnauthorizedException: Raised when TwichAPI return 401 status code.
            UserNotFoundException: Raised when TwichAPI return no user.

        Returns:
            TwichUserSchema: TwichUserSchema instance.
        """

        response: Response = get(
            f'{settings.TWICH_GET_USER_BASE_URL}?login={user_login}',
            headers=self._prepare_headers(),
        )

        if response.status_code == status.HTTP_400_BAD_REQUEST:
            raise GetUserBadRequestException

        if response.status_code == status.HTTP_401_UNAUTHORIZED:
            raise GetUserUnauthorizedException

        user_data: list = response.json().get('data')

        if not user_data:
            raise UserNotFoundException

        user: TwichUserSchema = TwichUserSchema(**user_data[0])

        # repository actions

        return user

    def parse_stream(self, user_login: str) -> TwichStreamSchema:
        """
        parse_stream: Parse stream data from the Twich.

        Args:
            user_login (str): Login of the user.

        Raises:
            GetStreamBadRequestException: Raised when TwichAPI return 400 status code.
            GetStreamUnauthorizedException: Raised when TwichAPI return 401 status code.
            StreamNotFoundException: Raised when TwichAPI return no stream.

        Returns:
            TwichStreamSchema: TwichStreamSchema instance.
        """

        response: Response = get(
            f'{settings.TWICH_GET_STREAM_BASE_URL}?user_login={user_login}',
            headers=self._prepare_headers(),
        )

        if response.status_code == status.HTTP_400_BAD_REQUEST:
            raise GetStreamBadRequestException

        if response.status_code == status.HTTP_401_UNAUTHORIZED:
            raise GetStreamUnauthorizedException

        stream_data: list = response.json().get('data')

        if not stream_data:
            raise StreamNotFoundException

        stream: TwichStreamSchema = TwichStreamSchema(**stream_data[0])

        # repository actions

        return stream
