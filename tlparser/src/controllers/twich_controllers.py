"""
twich_controllers.py: File, containing controllers for a twich app.
"""


from fastapi import HTTPException
from pydantic import ValidationError
from requests import Timeout, ConnectionError, RequestException, TooManyRedirects
from schemas.twich_schemas import TwichGameSchema, TwichUserSchema, TwichStreamSchema
from services.twich_services import TwichService
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


class TwichController:
    """
    TwichController: Class, that represents twich controller. It handles every http exception.
    """

    def __init__(self, twich_service: TwichService) -> None:
        """
        __init__: Initialize twich controller class.

        Args:
            twich_service (TwichService): TwichService instance.
        """

        self.service = twich_service

    def parse_game(self, game_name: str) -> TwichGameSchema:
        """
        parse_game: Delegate parsing to TwichService, catch and handle all exceptions.

        Args:
            game_name (str): Name of the game.

        Raises:
            HTTPException: Raised when TwichAPI exception is raised.
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

    def parse_user(self, user_login: str) -> TwichUserSchema:
        """
        parse_user: Delegate parsing to TwichService, catch and handle all exceptions.

        Args:
            user_login (str): Login of the user.

        Raises:
            HTTPException: Raised when TwichAPI exception is raised.
            HTTPException: Raised when ConnectionError exception is raised by requests.
            HTTPException: Raised when Timeout exception is raised by requests.
            HTTPException: Raised when TooManyRedirects exception is raised by requests.
            HTTPException: Raised when RequestException exception is raised by requests.
            HTTPException: Raised when ValidationError exception is raised by pydantic.
            HTTPException: Raised when Any other exception is raised.

        Returns:
            TwichUserSchema: TwichUserSchema instance.
        """

        try:
            return self.service.parse_user(user_login)
        except (GetUserBadRequestException, GetUserUnauthorizedException):
            raise HTTPException(status_code=503, detail='Service unavaliable (TwichAPI exception)')
        except UserNotFoundException:
            raise HTTPException(status_code=404, detail='User is not found')
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

    def parse_stream(self, user_login: str) -> TwichStreamSchema:
        """
        parse_stream: Delegate parsing to TwichService, catch and handle all exceptions.

        Args:
            user_login (str): Login of the user.

        Raises:
            HTTPException: Raised when TwichAPI exception is raised.
            HTTPException: Raised when ConnectionError exception is raised by requests.
            HTTPException: Raised when Timeout exception is raised by requests.
            HTTPException: Raised when TooManyRedirects exception is raised by requests.
            HTTPException: Raised when RequestException exception is raised by requests.
            HTTPException: Raised when ValidationError exception is raised by pydantic.
            HTTPException: Raised when Any other exception is raised.

        Returns:
            TwichStreamSchema: TwichStreamSchema instance.
        """

        try:
            return self.service.parse_stream(user_login)
        except (GetStreamBadRequestException, GetStreamUnauthorizedException):
            raise HTTPException(status_code=503, detail='Service unavaliable (TwichAPI exception)')
        except StreamNotFoundException:
            raise HTTPException(status_code=404, detail='Stream is not found (stream is off)')
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
