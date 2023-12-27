"""
stream_controller.py: File, containing twich stream controller.
"""


from fastapi import HTTPException
from pydantic import ValidationError
from requests import ConnectionError, RequestException, Timeout, TooManyRedirects
from domain.entities.twich.stream_entity import TwichStreamEntity
from domain.exceptions.twich.stream_exceptions import (
    GetStreamBadRequestException,
    GetStreamUnauthorizedException,
    StreamNotFoundException,
)
from domain.services.twich.stream_service import ITwichStreamService
from presentation.mappers.twich.stream_mapper import TwichStreamMapper
from presentation.schemas.twich.stream_schema import TwichStreamSchema


class TwichStreamController:
    """
    TwichStreamController: Class, representing twich stream controller. It handles all exceptions.
    """

    def __init__(self, service: ITwichStreamService) -> None:
        """
        __init__: Initialize twich stream controller class.

        Args:
            service (ITwichStreamService): Twich stream service abstract class.
        """

        self.service: ITwichStreamService = service

    async def parse_stream(self, user_login: str) -> None:
        """
        parse_stream: Called twich stream service to send event about parsing.

        Args:
            user_login (str): Login of the user.
        """

        await self.service.parse_stream(user_login)

    async def private_parse_stream(self, user_login: str) -> TwichStreamSchema:
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
            TwichStreamSchema: TwichStreamSchema instance.
        """

        try:
            stream: TwichStreamEntity = await self.service.private_parse_stream(user_login)
            return TwichStreamMapper.to_schema(stream)
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

    async def get_all_streams(self) -> list[TwichStreamSchema]:
        """
        get_all_streams: Delegate access to TwichStreamService, handle exceptions.

        Raises:
            HTTPException: Raised when Any other exception is raised.

        Returns:
            list[TwichStreamSchema]: List of twich streams.
        """

        try:
            streams: list[TwichStreamEntity] = await self.service.get_all_streams()
            return [TwichStreamMapper.to_schema(stream) for stream in streams]
        except Exception:
            raise HTTPException(status_code=503, detail='Service unavaliable (internal error)')

    async def get_stream_by_user_login(self, user_login: str) -> TwichStreamSchema:
        """
        get_stream_by_user_login: Delegate access to TwichStreamService, handle exceptions.

        Args:
            user_login (str): Login of the user.

        Raises:
            HTTPException: Raised when Stream is not found (stream is off).
            HTTPException: Raised when Any other exception is raised.

        Returns:
            TwichStreamSchema: TwichStreamSchema instance.
        """

        try:
            stream: TwichStreamEntity = await self.service.get_stream_by_user_login(user_login)
            return TwichStreamMapper.to_schema(stream)
        except StreamNotFoundException:
            raise HTTPException(status_code=404, detail='Stream is not found (stream is off)')
        except Exception:
            raise HTTPException(status_code=503, detail='Service unavaliable (internal error)')
