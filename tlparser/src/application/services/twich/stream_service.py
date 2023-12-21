"""
stream_service.py: File, containing service for a twich stream.
"""


from fastapi import status
from requests import Response, get
from application.dependencies.twich.token_dependency import TwichAPIToken
from application.exceptions.twich.stream_exceptions import (
    GetStreamBadRequestException,
    GetStreamUnauthorizedException,
    StreamNotFoundException,
)
from application.mappers.twich.stream_mapper import TwichStreamCreateMapper, TwichStreamReadMapper
from application.schemas.twich.stream_schema import TwichStreamCreateSchema, TwichStreamReadSchema
from common.config.twich.settings import settings
from domain.entities.twich.stream_entity import TwichStreamEntity
from domain.repositories.twich.stream_repository import TwichStreamRepository


class TwichStreamService:
    """
    TwichStreamService: Class, that contains business logic for twich streams.
    """

    def __init__(self, repository: TwichStreamRepository, token: TwichAPIToken) -> None:
        """
        __init__: Do some initialization for TwichStreamService class.

        Args:
            repository (TwichStreamRepository): Twich stream repository.
        """

        self.repository = repository
        self.access_token = token.access_token
        self.headers = token.headers

    def parse_stream(self, user_login: str) -> TwichStreamReadSchema:
        """
        parse_stream: Parse stream data from the Twich.

        Args:
            user_login (str): Login of the user.

        Raises:
            GetStreamBadRequestException: Raised when TwichAPI return 400 status code.
            GetStreamUnauthorizedException: Raised when TwichAPI return 401 status code.
            StreamNotFoundException: Raised when TwichAPI return no stream.

        Returns:
            TwichStreamReadSchema: TwichStreamReadSchema instance.
        """

        response: Response = get(
            f'{settings.TWICH_GET_STREAM_BASE_URL}?user_login={user_login}',
            headers=self.headers,
        )

        if response.status_code == status.HTTP_400_BAD_REQUEST:
            raise GetStreamBadRequestException

        if response.status_code == status.HTTP_401_UNAUTHORIZED:
            raise GetStreamUnauthorizedException

        stream_data: list = response.json().get('data')

        if not stream_data:
            raise StreamNotFoundException

        stream_schema: TwichStreamCreateSchema = TwichStreamCreateSchema(**stream_data[0])

        stream_entity: TwichStreamEntity = self.repository.create_or_update(
            TwichStreamCreateMapper.to_domain(stream_schema),
        )

        return TwichStreamReadMapper.to_schema(stream_entity)

    def delete_stream_by_user_login(self, user_login: str) -> None:
        """
        delete_stream_by_user_login: Delete twich stream.

        Args:
            user_login (str): Login of the user.
        """

        self.repository.delete_stream_by_user_login(user_login)

        return

    def get_all_streams(self) -> list[TwichStreamReadSchema]:
        """
        get_all_streams: Return all twich streams.

        Returns:
            list[TwichStreamReadSchema]: List of twich streams.
        """

        return [
            TwichStreamReadMapper.to_schema(stream_entity)
            for stream_entity in self.repository.all()
        ]

    def get_stream_by_user_login(self, user_login: str) -> TwichStreamReadSchema:
        """
        get_stream_by_user_login _summary_

        Args:
            user_login (str): _description_

        Returns:
            TwichStreamReadSchema: TwichStreamReadSchema instance.
        """

        stream_entity: TwichStreamEntity = self.repository.get_stream_by_user_login(user_login)

        return TwichStreamReadMapper.to_schema(stream_entity)
