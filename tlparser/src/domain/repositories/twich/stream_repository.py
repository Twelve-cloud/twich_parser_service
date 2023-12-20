"""
stream_repository.py: File, containing repository abstract class for a twich stream.
"""


from abc import abstractmethod
from domain.entities.twich.stream_entity import TwichStreamEntity
from domain.repositories.base.base_repository import BaseRepository


class TwichStreamRepository(BaseRepository[TwichStreamEntity]):
    """
    TwichStreamRepository: Abstract class for twich stream repositories.

    Args:
        BaseRepository (TwichStreamEntity): BaseRepository for TwichStreamRepository.
    """

    @abstractmethod
    def delete_stream_by_user_login(self, user_login: str) -> None:
        """
        delete_stream_by_user_login: Delete stream by user login.

        Args:
            user_login (str): Login of the user.
        """

        pass

    @abstractmethod
    def get_stream_by_user_login(self, user_login: str) -> TwichStreamEntity:
        """
        get_stream_by_user_login: Return stream by user login.

        Args:
            user_login (str): Login of the user.

        Returns:
            TwichStreamEntity: Twich stream entity.
        """

        pass
