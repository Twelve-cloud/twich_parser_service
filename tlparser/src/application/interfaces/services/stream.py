"""
stream.py: File, containing service interface for a twich stream.
"""


from abc import abstractmethod
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
from application.interfaces.services import IBaseService


class ITwichStreamService(IBaseService):
    """
    ITwichStreamService: Class that represents service interface for a twich stream.

    Args:
        IBaseService: Base service interface.
    """

    @abstractmethod
    async def parse_stream(
        self,
        request: ParseTwichStreamRequest,
    ) -> ParseTwichStreamResponse:
        """
        parse_stream: Should parse twich stream.
        Must be overriden.

        Args:
            request (ParseTwichGameRequest): Request about parsing twich stream.

        Returns:
            ParseTwichStreamResponse: Response about parsing twich stream.
        """

        pass

    @abstractmethod
    async def delete_stream_by_user_login(
        self,
        request: DeleteTwichStreamByUserLoginRequest,
    ) -> DeleteTwichStreamByUserLoginResponse:
        """
        delete_stream_by_user_login: Should delete twich stream.
        Must be overriden.

        Args:
            request (DeleteTwichStreamByUserLoginRequest): Request about deleting twich stream.

        Returns:
            DeleteTwichStreamByUserLoginResponse: Response about deleting twich stream.
        """

        pass

    @abstractmethod
    async def get_all_streams(
        self,
    ) -> list[GetTwichStreamByUserLoginResponse]:
        """
        get_all_streams: Should return all twich streams.
        Must be overriden.

        Returns:
            list[GetTwichStreamByUserLoginResponse]: List of responses about getting twich stream.
        """

        pass

    @abstractmethod
    async def get_stream_by_user_login(
        self,
        request: GetTwichStreamByUserLoginRequest,
    ) -> GetTwichStreamByUserLoginResponse:
        """
        get_stream_by_user_login: Should return twich game.
        Must be overriden.

        Args:
            request (GetTwichStreamByUserLoginRequest): Request about getting twich stream.

        Returns:
            GetTwichStreamByUserLoginResponse: Response about getting twich stream.
        """

        pass
