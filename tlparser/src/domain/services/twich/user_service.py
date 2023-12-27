"""
user_service.py: File, containing twich user service abstract class.
"""


from abc import abstractmethod
from domain.entities.twich.user_entity import TwichUserEntity
from domain.services.base.base_service import IBaseService


class ITwichUserService(IBaseService):
    """
    ITwichUserService: Class, that represents abstract class for twich user service.

    Args:
        IBaseService (_type_): Base abstract class for twich user abstract class.
    """

    @abstractmethod
    async def parse_user(self, user_login: str) -> None:
        """
        parse_user: Called twich user publisher to publish event about parsing.

        Args:
            user_login (str): Login of the user.
        """

        pass

    @abstractmethod
    async def private_parse_user(self, user_login: str) -> TwichUserEntity:
        """
        private_parse_user: Parse user data from the Twich.

        Args:
            user_login (str): Login of the user.

        Raises:
            GetUserBadRequestException: Raised when TwichAPI return 400 status code.
            GetUserUnauthorizedException: Raised when TwichAPI return 401 status code.
            UserNotFoundException: Raised when TwichAPI return no user.

        Returns:
            TwichUserEntity: TwichUserEntity instance.
        """

        pass

    @abstractmethod
    async def delete_user_by_login(self, user_login: str) -> None:
        """
        delete_user_by_login: Delete twich user.

        Args:
            user_login (str): Login of the user.
        """

        pass

    @abstractmethod
    async def get_all_users(self) -> list[TwichUserEntity]:
        """
        get_all_users: Return list of twich users.

        Returns:
            list[TwichUserEntity]: List of twich users.
        """

        pass

    @abstractmethod
    async def get_user_by_login(self, user_login: str) -> TwichUserEntity:
        """
        get_user_by_login: Return user by login.

        Args:
            user_login (str): Login of the user.

        Returns:
            TwichUserEntity: TwichUserEntity instance.
        """

        pass
