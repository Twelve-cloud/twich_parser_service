"""
user_controller.py: File, containing twich user controller.
"""


from fastapi import HTTPException
from pydantic import ValidationError
from requests import ConnectionError, RequestException, Timeout, TooManyRedirects
from application.exceptions.twich.user_exceptions import (
    GetUserBadRequestException,
    GetUserUnauthorizedException,
    UserNotFoundException,
)
from application.schemas.twich.user_schema import TwichUserReadSchema
from application.services.twich.user_service import TwichUserService


class TwichUserController:
    """
    TwichUserController: Class, representing twich user controller. It handles all exceptions.
    """

    def __init__(self, service: TwichUserService) -> None:
        """
        __init__: Initialize twich user controller class.

        Args:
            service (TwichUserService): TwichUserService instance.
        """

        self.service = service

    def parse_user(self, user_login: str) -> None:
        """
        parse_user: Called twich user service to send event about parsing.

        Args:
            user_login (str): Login of the user.
        """

        self.service.parse_user(user_login)

    def private_parse_user(self, user_login: str) -> TwichUserReadSchema:
        """
        private_parse_user: Delegate parsing to TwichUserService, handle exceptions.

        Args:
            user_login (str): Login of the user.

        Raises:
            HTTPException: Raised when TwichAPI exception is raised.
            HTTPException: Raised when User is not found.
            HTTPException: Raised when ConnectionError exception is raised by requests.
            HTTPException: Raised when Timeout exception is raised by requests.
            HTTPException: Raised when TooManyRedirects exception is raised by requests.
            HTTPException: Raised when RequestException exception is raised by requests.
            HTTPException: Raised when ValidationError exception is raised by pydantic.
            HTTPException: Raised when Any other exception is raised.

        Returns:
            TwichUserReadSchema: TwichUserReadSchema instance.
        """

        try:
            return self.service.private_parse_user(user_login)
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

    def delete_user_by_login(self, user_login: str) -> None:
        """
        delete_user_by_login: Delegate deleting to TwichUserService, handle exceptions.

        Args:
            user_login (str): Login of the user.

        Raises:
            HTTPException: Raised when Any other exception is raised.
        """

        try:
            return self.service.delete_user_by_login(user_login)
        except Exception:
            raise HTTPException(status_code=503, detail='Service unavaliable (internal error)')

    def get_all_users(self) -> list[TwichUserReadSchema]:
        """
        get_all_users: Delegate access to TwichUserService, handle exceptions.

        Raises:
            HTTPException: Raised when Any other exception is raised.

        Returns:
            list[TwichUserReadSchema]: List of twich users.
        """

        try:
            return self.service.get_all_users()
        except Exception:
            raise HTTPException(status_code=503, detail='Service unavaliable (internal error)')

    def get_user_by_login(self, user_login: str) -> TwichUserReadSchema:
        """
        get_user_by_login: Delegate access to TwichUserService, handle exceptions.

        Args:
            user_login (str): Login of the user.

        Raises:
            HTTPException: Raised when User is not found.
            HTTPException: Raised when Any other exception is raised.

        Returns:
            TwichUserReadSchema: TwichUserReadSchema instance.
        """

        try:
            return self.service.get_user_by_login(user_login)
        except UserNotFoundException:
            raise HTTPException(status_code=404, detail='User is not found')
        except Exception:
            raise HTTPException(status_code=503, detail='Service unavaliable (internal error)')
