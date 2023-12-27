"""
stream_controller.py: File, containing twich stream controller.
"""


from fastapi import HTTPException
from pydantic import ValidationError
from requests import ConnectionError, RequestException, Timeout, TooManyRedirects
from application.schemas.twich.stream_schema import TwichStreamReadSchema
from application.services.twich.stream_service import TwichStreamService
from domain.exceptions.twich.stream_exceptions import (
    GetStreamBadRequestException,
    GetStreamUnauthorizedException,
    StreamNotFoundException,
)


class TwichStreamController:
    """
    TwichStreamController: Class, representing twich stream controller. It handles all exceptions.
    """

    def __init__(self, service: TwichStreamService) -> None:
        """
        __init__: Initialize twich stream controller class.

        Args:
            service (TwichStreamService): TwichStreamService instance.
        """

        self.service: TwichStreamService = service

    async def parse_stream(self, user_login: str) -> None:
        """
        parse_stream: Called twich stream service to send event about parsing.

        Args:
            user_login (str): Login of the user.
        """

        await self.service.parse_stream(user_login)

    async def private_parse_stream(self, user_login: str) -> TwichStreamReadSchema:
        """
        private_parse_stream: Delegate parsing to TwichStreamService, catch and handle exceptions.

        Args:
            user_login (str): Login of the user.

        Raises:
            HTTPException: Raised when TwichAPI exception is raised.
            HTTPException: Raised when Stream is not found (stream is off).
            HTTPException: Raised when ConnectionError exception is raised by requests.
            HTTPException: Raised when Timeout exception is raised by requests.
            HTTPException: Raised when TooManyRedirects exception is raised by requests.
            HTTPException: Raised when RequestException exception is raised by requests.
            HTTPException: Raised when ValidationError exception is raised by pydantic.
            HTTPException: Raised when Any other exception is raised.

        Returns:
            TwichStreamReadSchema: TwichStreamReadSchema instance.
        """

        try:
            return await self.service.private_parse_stream(user_login)
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

    async def delete_stream_by_user_login(self, user_login: str) -> None:
        """
        delete_stream_by_user_login: Delegate deleting to TwichStreamService, handle exceptions.

        Args:
            user_login (str): Login of the user.

        Raises:
            HTTPException: Raised when Any other exception is raised.
        """

        try:
            return await self.service.delete_stream_by_user_login(user_login)
        except Exception:
            raise HTTPException(status_code=503, detail='Service unavaliable (internal error)')

    async def get_all_streams(self) -> list[TwichStreamReadSchema]:
        """
        get_all_streams: Delegate access to TwichStreamService, handle exceptions.

        Raises:
            HTTPException: Raised when Any other exception is raised.

        Returns:
            list[TwichStreamReadSchema]: List of twich streams.
        """

        try:
            return await self.service.get_all_streams()
        except Exception:
            raise HTTPException(status_code=503, detail='Service unavaliable (internal error)')

    async def get_stream_by_user_login(self, user_login: str) -> TwichStreamReadSchema:
        """
        get_stream_by_user_login: Delegate access to TwichStreamService, handle exceptions.

        Args:
            user_login (str): Login of the user.

        Raises:
            HTTPException: Raised when Stream is not found (stream is off).
            HTTPException: Raised when Any other exception is raised.

        Returns:
            TwichStreamReadSchema: TwichStreamReadSchema instance.
        """

        try:
            return await self.service.get_stream_by_user_login(user_login)
        except StreamNotFoundException:
            raise HTTPException(status_code=404, detail='Stream is not found (stream is off)')
        except Exception:
            raise HTTPException(status_code=503, detail='Service unavaliable (internal error)')
