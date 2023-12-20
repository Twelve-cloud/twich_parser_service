"""
game_controller.py: File, containing twich game controller.
"""


from application.exceptions.twich.game_exceptions import (
    GameNotFoundException,
    GetGameBadRequestException,
    GetGameUnauthorizedException,
)
from application.schemas.twich.game_schema import TwichGameReadSchema
from application.services.twich.game_service import TwichGameService
from fastapi import HTTPException
from pydantic import ValidationError
from requests import ConnectionError, RequestException, Timeout, TooManyRedirects


class TwichGameController:
    """
    TwichGameController: Class, representing twich game controller. It handles all exceptions.
    """

    def __init__(self, service: TwichGameService) -> None:
        """
        __init__: Initialize twich game controller class.

        Args:
            service (TwichGameService): TwichGameService instance.
        """

        self.service = service

    def parse_game(self, game_name: str) -> TwichGameReadSchema:
        """
        parse_game: Delegate parsing to TwichGameService, handle exceptions.

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
            TwichGameReadSchema: TwichGameReadSchema instance.
        """

        try:
            return self.service.parse_game(game_name)
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

    def delete_game_by_name(self, game_name: str) -> None:
        """
        delete_game_by_name: Delegate deleting to TwichGameService, handle exceptions.

        Args:
            game_name (str): Name of the game.

        Raises:
            HTTPException: Raised when Any other exception is raised.
        """

        try:
            return self.service.delete_game_by_name(game_name)
        except Exception:
            raise HTTPException(status_code=503, detail='Service unavaliable (internal error)')

    def get_all_games(self) -> list[TwichGameReadSchema]:
        """
        get_all_games: Delegate access to TwichGameService, handle exceptions.

        Raises:
            HTTPException: Raised when Any other exception is raised.

        Returns:
            list[TwichGameReadSchema]: List of games.
        """

        try:
            return self.service.get_all_games()
        except Exception:
            raise HTTPException(status_code=503, detail='Service unavaliable (internal error)')

    def get_game_by_name(self, game_name: str) -> TwichGameReadSchema:
        """
        get_game_by_name: Delegate access to TwichGameService, handle exceptions.

        Args:
            game_name (str): Name of the game.

        Raises:
            HTTPException: Raised when Game is not found.
            HTTPException: Raised when Any other exception is raised.

        Returns:
            TwichGameReadSchema: TwichGameReadSchema instance.
        """

        try:
            return self.service.get_game_by_name(game_name)
        except GameNotFoundException:
            raise HTTPException(status_code=404, detail='Game is not found')
        except Exception:
            raise HTTPException(status_code=503, detail='Service unavaliable (internal error)')
