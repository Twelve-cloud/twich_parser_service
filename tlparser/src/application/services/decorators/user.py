"""
user.py: File, containing service implementation for a twich user.
"""


from automapper import mapper
from application.dtos.requests import (
    DeleteTwichUserByLoginRequest,
    GetTwichUserByLoginRequest,
    ParseTwichUserRequest,
)
from application.dtos.responses import (
    DeleteTwichUserByLoginResponse,
    GetTwichUserByLoginResponse,
    ParseTwichUserResponse,
)
from application.interfaces.services import ITwichUserService
from domain.interfaces.parsers import ITwichUserParser
from domain.interfaces.publishers import ITwichUserPublisher
from domain.interfaces.repositories import ITwichUserRepository
from domain.models import TwichUser


class TwichUserService(ITwichUserService):
    """
    TwichUserService: Class, that represents implementation of twich user service interface.
    That class unites presentation layer and infrastructure layer with domain layer.
    It calls repository, publisher and parser and return responses to controllers.
    """

    def __init__(
        self,
        parser: ITwichUserParser,
        publisher: ITwichUserPublisher,
        repository: ITwichUserRepository,
    ) -> None:
        """
        __init__: Initialize twich user service implementation class.

        Args:
            parser (ITwichUserParser): Twich user parser.
            publisher (ITwichUserPublisher): Twich user publisher.
            repository (ITwichUserRepository): Twich user repository.
        """

        self.parser: ITwichUserParser = parser
        self.publisher: ITwichUserPublisher = publisher
        self.repository: ITwichUserRepository = repository

    async def parse_user(
        self,
        request: ParseTwichUserRequest,
    ) -> ParseTwichUserResponse:
        """
        parse_user: Parse twich user and add it to repository.
        Also publish message about creating twich user.

        Args:
            request (ParseTwichUserRequest): Request about parsing twich user.

        Returns:
            ParseTwichUserResponse: Response about parsing twich user.
        """

        user: TwichUser = await self.parser.parse_user(**request.dict())
        await self.repository.add_or_update(user)
        await self.publisher.publish(user.events)

        return mapper.to(ParseTwichUserResponse).map(user)

    async def delete_user_by_login(
        self,
        request: DeleteTwichUserByLoginRequest,
    ) -> DeleteTwichUserByLoginResponse:
        """
        delete_user_by_login: Delete twich user and remove it from repository.
        Also publish message about deleting twich user.

        Args:
            request (DeleteTwichUserByLoginRequest): Request about deleting twich user.

        Returns:
            DeleteTwichUserByLoginResponse: Response about deleting twich user.
        """

        user: TwichUser = await self.repository.get_user_by_login(**request.dict())
        user.delete()
        await self.repository.delete(user)
        await self.publisher.publish(user.events)

        return DeleteTwichUserByLoginResponse(status='OK')

    async def get_all_users(
        self,
    ) -> list[GetTwichUserByLoginResponse]:
        """
        get_all_users: Return all twich users.

        Returns:
            list[GetTwichUserByLoginResponse]: List of responses about getting twich user.
        """

        users: list[TwichUser] = await self.repository.all()

        return [mapper.to(GetTwichUserByLoginResponse).map(user) for user in users]

    async def get_user_by_login(
        self,
        request: GetTwichUserByLoginRequest,
    ) -> GetTwichUserByLoginResponse:
        """
        get_user_by_login: Return twich user.

        Args:
            request (GetTwichUserByLoginRequest): Request about getting twich user.

        Returns:
            GetTwichUserByLoginResponse: Response about gettings twich user.
        """

        user: TwichUser = await self.repository.get_user_by_login(**request.dict())

        return mapper.to(GetTwichUserByLoginResponse).map(user)
