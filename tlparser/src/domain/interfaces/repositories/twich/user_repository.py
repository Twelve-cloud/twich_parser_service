"""
user_repository.py: File, containing repository abstract class for a twich user.
"""


from abc import abstractmethod
from domain.entities.twich.user_entity import TwichUserEntity
from domain.events.twich.user_events import (
    PublicParseUserCalledEvent,
    TwichUserCreatedOrUpdatedEvent,
    TwichUserDeletedByLoginEvent,
)
from domain.interfaces.repositories.base.base_repository import IBaseRepository


class ITwichUserRepository(IBaseRepository[TwichUserEntity, TwichUserCreatedOrUpdatedEvent]):
    """
    ITwichUserRepository: Abstract class for twich user repositories.

    Args:
        IBaseRepository (TwichUserEntity): IBaseRepository for ITwichUserRepository.
    """

    @abstractmethod
    async def parse_user(self, login: str) -> PublicParseUserCalledEvent:
        """
        parse_user: Return event about parsing twich user.

        Args:
            login (str): Login of the user.

        Returns:
            PublicParseUserCalledEvent: Event about parsing twich user.
        """

        pass

    @abstractmethod
    async def delete_user_by_login(self, login: str) -> TwichUserDeletedByLoginEvent:
        """
        delete_user_by_login: Delete user by login.

        Args:
            login (str): Login of the user.

        Returns:
            TwichUserDeletedByLoginEvent: Event about deleting twich user.
        """

        pass

    @abstractmethod
    async def get_user_by_login(self, login: str) -> TwichUserEntity:
        """
        get_user_by_login: Return user by login.

        Args:
            login (str): Login of the user.

        Returns:
            TwichUserEntity: Twich user entity.
        """

        pass