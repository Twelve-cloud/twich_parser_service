"""
game_service.py: File, containing domain service for a twich game.
"""


from typing import Optional
from aiohttp import ClientSession
from fastapi import status
from common.config.twich.settings import settings
from domain.dependencies.twich.token_dependency import TwichAPIToken
from domain.entities.twich.game_entity import TwichGameEntity
from domain.exceptions.twich.game_exceptions import (
    GameNotFoundException,
    GetGameBadRequestException,
    GetGameUnauthorizedException,
)


class TwichGameDomainService:
    """
    TwichGameDomainService: Class, that contains business logic for twich games.
    """

    def __init__(self, token: TwichAPIToken) -> None:
        """
        __init__: Do some initialization for TwichGameDomainService class.

        Args:
            token (TwichAPIToken): Token for twich api.
        """

        self.access_token: str = token.access_token
        self.headers: dict[str, str] = token.headers

    async def parse_game(self, game_name: str) -> TwichGameEntity:
        """
        parse_game: Parse game data from the Twich.

        Args:
            game_name (str): Name of the game.

        Raises:
            GetGameBadRequestException: Raised when TwichAPI return 400 status code.
            GetGameUnauthorizedException: Raised when TwichAPI return 401 status code.
            GameNotFoundException: Raised when TwichAPI return no game.

        Returns:
            TwichGameEntity: TwichGameEntity instance.
        """

        async with ClientSession() as session:
            async with session.get(
                f'{settings.TWICH_GET_GAME_BASE_URL}?name={game_name}',
                headers=self.headers,
            ) as response:
                if response.status == status.HTTP_400_BAD_REQUEST:
                    raise GetGameBadRequestException

                if response.status == status.HTTP_401_UNAUTHORIZED:
                    raise GetGameUnauthorizedException

                game_data: Optional[dict] = await response.json()

                if not game_data:
                    raise GameNotFoundException

                game: Optional[list] = game_data.get('data')

                if not game:
                    raise GameNotFoundException

                game_entity: TwichGameEntity = TwichGameEntity(**game[0])

                return game_entity
