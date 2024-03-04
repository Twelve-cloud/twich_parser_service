"""
stream.py: File, containing service implementation for a twich stream.
"""


from automapper import mapper
from application.dtos.requests import (
    DeleteTwichStreamByUserLoginRequest,
    GetTwichStreamByUserLoginRequest,
    ParseTwichStreamRequest,
)
from application.dtos.responses import (
    DeleteTwichStreamByUserLoginResponse,
    GetTwichStreamByUserLoginResponse,
    ParseTwichStreamResponse,
)
from application.interfaces.services import ITwichStreamService
from domain.interfaces.parsers import ITwichStreamParser
from domain.interfaces.publishers import ITwichStreamPublisher
from domain.interfaces.repositories import ITwichStreamRepository
from domain.models import TwichStream


class TwichStreamService(ITwichStreamService):
    """
    TwichStreamService: Class, that represents implementation of twich stream service interface.
    That class unites presentation layer and infrastructure layer with domain layer.
    It calls repository, publisher and parser and return responses to controllers.
    """

    def __init__(
        self,
        parser: ITwichStreamParser,
        publisher: ITwichStreamPublisher,
        repository: ITwichStreamRepository,
    ) -> None:
        """
        __init__: Initialize twich stream service implementation class.

        Args:
            parser (ITwichStreamParser): Twich stream parser.
            publisher (ITwichStreamPublisher): Twich stream publisher.
            repository (ITwichStreamRepository): Twich stream repository.
        """

        self.parser: ITwichStreamParser = parser
        self.publisher: ITwichStreamPublisher = publisher
        self.repository: ITwichStreamRepository = repository

    async def parse_stream(
        self,
        request: ParseTwichStreamRequest,
    ) -> ParseTwichStreamResponse:
        """
        parse_stream: Parse twich stream and add it to repository.
        Also publish message about creating twich stream.

        Args:
            request (ParseTwichStreamRequest): Request about parsing twich stream.

        Returns:
            ParseTwichStreamResponse: Response about parsing twich stream.
        """

        stream: TwichStream = await self.parser.parse_stream(**request.dict())
        await self.repository.add_or_update(stream)
        await self.publisher.publish(stream.events)

        return mapper.to(ParseTwichStreamResponse).map(stream)

    async def delete_stream_by_user_login(
        self,
        request: DeleteTwichStreamByUserLoginRequest,
    ) -> DeleteTwichStreamByUserLoginResponse:
        """
        delete_stream_by_user_login: Delete twich stream and remove it from repository.
        Also publish message about deleting twich stream.

        Args:
            request (DeleteTwichStreamByUserLoginRequest): Request about deleting twich stream.

        Returns:
            DeleteTwichStreamByUserLoginResponse: Response about deleting twich stream.
        """

        stream: TwichStream = await self.repository.get_stream_by_user_login(**request.dict())
        stream.delete()
        await self.repository.delete(stream)
        await self.publisher.publish(stream.events)

        return DeleteTwichStreamByUserLoginResponse(status='OK')

    async def get_all_streams(
        self,
    ) -> list[GetTwichStreamByUserLoginResponse]:
        """
        get_all_streams: Return all twich streams.

        Returns:
            list[GetTwichStreamByUserLoginResponse]: List of responses about getting twich stream.
        """

        streams: list[TwichStream] = await self.repository.all()

        return [mapper.to(GetTwichStreamByUserLoginResponse).map(stream) for stream in streams]

    async def get_stream_by_user_login(
        self,
        request: GetTwichStreamByUserLoginRequest,
    ) -> GetTwichStreamByUserLoginResponse:
        """
        get_stream_by_user_login: Return twich stream.

        Args:
            request (GetTwichStreamByUserLoginRequest): Request about getting twich stream.

        Returns:
            GetTwichStreamByUserLoginResponse: Response about gettings twich stream.
        """

        stream: TwichStream = await self.repository.get_stream_by_user_login(**request.dict())

        return mapper.to(GetTwichStreamByUserLoginResponse).map(stream)
