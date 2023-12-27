"""
stream_service: File, containing twich stream service abstract class.
"""


from abc import abstractmethod
from domain.entities.twich.stream_entity import TwichStreamEntity
from domain.services.base.base_service import IBaseService


class ITwichStreamService(IBaseService):
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
    async def private_parse_stream(self, user_login: str) -> TwichStreamEntity:
        """
        private_parse_stream: Parse stream data from the Twich.

        Args:
            user_login (str): Login of the user.

        Returns:
            TwichStreamEntity: TwichStreamEntity instance.
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
    async def get_all_streams(self) -> list[TwichStreamEntity]:
        """
        get_all_streams: Return all twich streams.

        Returns:
            list[TwichStreamEntity]: List of twich streams.
        """

        pass

    @abstractmethod
    async def get_stream_by_user_login(self, user_login: str) -> TwichStreamEntity:
        """
        get_stream_by_user_login _summary_

        Args:
            user_login (str): _description_

        Returns:
            TwichStreamEntity: TwichStreamEntity instance.
        """

        pass
