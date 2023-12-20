"""
user_repository.py: File, containing repository abstract class for a twich user.
"""


from abc import abstractmethod
from domain.entities.twich.user_entity import TwichUserEntity
from domain.repositories.base.base_repository import BaseRepository


class TwichUserRepository(BaseRepository[TwichUserEntity]):
    """
    TwichUserRepository: Abstract class for twich user repositories.

    Args:
        BaseRepository (TwichUserEntity): BaseRepository for TwichUserRepository.
    """

    def delete_user_by_login(self, login: str) -> None:
        """
        delete_user_by_login: Delete user by login.

        Args:
            login (str): Login of the user.
        """

        pass

    @abstractmethod
    def get_user_by_login(self, login: str) -> TwichUserEntity:
        """
        get_user_by_login: Return user by login.

        Args:
            login (str): Login of the user.

        Returns:
            TwichUserEntity: Twich user entity.
        """

        pass
