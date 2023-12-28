"""
stream_service: File, containing twich stream service abstract class.
"""


from abc import abstractmethod
from application.interfaces.services.base.base_service import IBaseService
from application.schemas.twich.stream_schema import TwichStreamSchema


class ITwichStreamService(IBaseService[TwichStreamSchema]):
    """
    ITwichStreamService: Class, that represents abstract class for twich stream service.

    Args:
        IBaseService (_type_): Base abstract class for twich stream abstract class.
    """

    @abstractmethod
    async def parse_stream(self, user_login: str) -> None:
        """
        parse_stream: Called twich stream publisher to publish event about parsing.

        Args:
            user_login (str): Login of the user.
        """

        pass

    @abstractmethod
    async def private_parse_stream(self, user_login: str) -> TwichStreamSchema:
        """
        private_parse_stream: Parse stream data from the Twich.

        Args:
            user_login (str): Login of the user.

        Returns:
            TwichStreamSchema: TwichStreamSchema instance.
        """

        pass

    @abstractmethod
    async def delete_stream_by_user_login(self, user_login: str) -> None:
        """
        delete_stream_by_user_login: Delete twich stream.

        Args:
            user_login (str): Login of the user.
        """

        pass

    @abstractmethod
    async def get_all_streams(self) -> list[TwichStreamSchema]:
        """
        get_all_streams: Return all twich streams.

        Returns:
            list[TwichStreamSchema]: List of twich streams.
        """

        pass

    @abstractmethod
    async def get_stream_by_user_login(self, user_login: str) -> TwichStreamSchema:
        """
        get_stream_by_user_login _summary_

        Args:
            user_login (str): _description_

        Returns:
            TwichStreamSchema: TwichStreamSchema instance.
        """

        pass
