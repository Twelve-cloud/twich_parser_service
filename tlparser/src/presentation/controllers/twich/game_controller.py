"""
game_controller.py: File, containing twich game controller.
"""


from fastapi import HTTPException
from pydantic import ValidationError
from requests import ConnectionError, RequestException, Timeout, TooManyRedirects
from application.interfaces.services.twich.game_service import ITwichGameService
from application.schemas.twich.game_schema import TwichGameSchema
from domain.exceptions.twich.game_exceptions import (
    GameNotFoundException,
    GetGameBadRequestException,
    GetGameUnauthorizedException,
)


class TwichGameController:
    """
    TwichGameController: Class, representing twich game controller. It handles all exceptions.
    """

    def __init__(self, service: ITwichGameService) -> None:
        """
        __init__: Initialize twich game controller class.

        Args:
            service (ITwichGameService): Twich game service abstract class.
        """

        self.service: ITwichGameService = service

    async def parse_game(self, game_name: str) -> None:
        """
        parse_game: Called twich game service to send event about parsing.

        Args:
            game_name (str): Name of the game.
        """

        await self.service.parse_game(game_name)

    async def private_parse_game(self, game_name: str) -> TwichGameSchema:
        """
        private_parse_game: Delegate parsing to TwichGameService, handle exceptions.

        Args:
            game_name (str): Name of the game.

        Raises:
            HTTPException: Raised when TwichAPI exception is raised.
            HTTPException: Raised when Game is not found.
            HTTPException: Raised when ConnectionError exception is raised by requests.
            HTTPException: Raised when Timeout exception is raised by requests.
            HTTPException: Raised when TooManyRedirects exception is raised by requests.
            HTTPException: Raised when RequestException exception is raised by requests.
            HTTPException: Raised when ValidationError exception is raised by pydantic.
            HTTPException: Raised when Any other exception is raised.

        Returns:
            TwichGameSchema: TwichGameSchema instance.
        """

        try:
            return await self.service.private_parse_game(game_name)
        except (GetGameBadRequestException, GetGameUnauthorizedException):
            raise HTTPException(status_code=503, detail='Service unavaliable (TwichAPI exception)')
        except GameNotFoundException:
            raise HTTPException(status_code=404, detail='Game is not found')
        except ConnectionError:
            raise HTTPException(status_code=503, detail='Service unavaliable (connection issues)')
        except Timeout:
            raise HTTPException(status_code=503, detail='Service unavaliable (request timeout)')
        except TooManyRedirects:
            raise HTTPException(status_code=503, detail='Service unavaliable (too many redirects)')
        except RequestException:
            raise HTTPException(status_code=503, detail='Service unavaliable (requests error)')
        except ValidationError:
            raise HTTPException(status_code=400, detail='Validation error (parsing error)')
        except Exception:
            raise HTTPException(status_code=503, detail='Service unavaliable (internal error)')

    async def delete_game_by_name(self, game_name: str) -> None:
        """
        delete_game_by_name: Delegate deleting to TwichGameService, handle exceptions.

        Args:
            game_name (str): Name of the game.

        Raises:
            HTTPException: Raised when Any other exception is raised.
        """

        try:
            return await self.service.delete_game_by_name(game_name)
        except Exception:
            raise HTTPException(status_code=503, detail='Service unavaliable (internal error)')

    async def get_all_games(self) -> list[TwichGameSchema]:
        """
        get_all_games: Delegate access to TwichGameService, handle exceptions.

        Raises:
            HTTPException: Raised when Any other exception is raised.

        Returns:
            list[TwichGameSchema]: List of games.
        """

        try:
            return await self.service.get_all_games()
        except Exception:
            raise HTTPException(status_code=503, detail='Service unavaliable (internal error)')

    async def get_game_by_name(self, game_name: str) -> TwichGameSchema:
        """
        get_game_by_name: Delegate access to TwichGameService, handle exceptions.

        Args:
            game_name (str): Name of the game.

        Raises:
            HTTPException: Raised when Game is not found.
            HTTPException: Raised when Any other exception is raised.

        Returns:
            TwichGameSchema: TwichGameSchema instance.
        """

        try:
            return await self.service.get_game_by_name(game_name)
        except GameNotFoundException:
            raise HTTPException(status_code=404, detail='Game is not found')
        except Exception:
            raise HTTPException(status_code=503, detail='Service unavaliable (internal error)')
