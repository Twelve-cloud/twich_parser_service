"""
user.py: File, containing service interface for a twich user.
"""


from abc import abstractmethod
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
from application.interfaces.services import IBaseService


class ITwichUserService(IBaseService):
    """
    ITwichUserService: Class that represents service interface for a twich user.

    Args:
        IBaseService: Base service interface.
    """

    @abstractmethod
    async def parse_user(
        self,
        request: ParseTwichUserRequest,
    ) -> ParseTwichUserResponse:
        """
        parse_user: Should parse twich user.
        Must be overriden.

        Args:
            request (ParseTwichUserRequest): Request about parsing twich user.

        Returns:
            ParseTwichUserResponse: Response about parsing twich user.
        """

        pass

    @abstractmethod
    async def delete_user_by_login(
        self,
        request: DeleteTwichUserByLoginRequest,
    ) -> DeleteTwichUserByLoginResponse:
        """
        delete_user_by_login: Should delete twich user.
        Must be overriden.

        Args:
            request (DeleteTwichUserByLoginRequest): Request about deleting twich user.

        Returns:
            DeleteTwichUserByLoginResponse: Response about deleting twich user.
        """

        pass

    @abstractmethod
    async def get_all_users(
        self,
    ) -> list[GetTwichUserByLoginResponse]:
        """
        get_all_users: Should return all twich users.
        Must be overriden.

        Returns:
            list[GetTwichUserByLoginResponse]: List of responses about getting twich user.
        """

        pass

    @abstractmethod
    async def get_user_by_login(
        self,
        request: GetTwichUserByLoginRequest,
    ) -> GetTwichUserByLoginResponse:
        """
        get_user_by_login: Should return twich user.
        Must be overriden.

        Args:
            request (GetTwichUserByLoginRequest): Request about getting twich user.

        Returns:
            GetTwichUserByLoginResponse: Response about gettings twich user.
        """

        pass
