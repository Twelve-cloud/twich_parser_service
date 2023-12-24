"""
stream_repository.py: File, containing repository abstract class for a twich stream.
"""


from abc import abstractmethod
from domain.entities.twich.stream_entity import TwichStreamEntity
from domain.events.twich.stream_events import (
    PublicParseStreamCalledEvent,
    TwichStreamCreatedOrUpdatedEvent,
    TwichStreamDeletedByUserLoginEvent,
)
from domain.repositories.base.base_repository import BaseRepository


class TwichStreamRepository(BaseRepository[TwichStreamEntity, TwichStreamCreatedOrUpdatedEvent]):
    """
    TwichStreamRepository: Abstract class for twich stream repositories.

    Args:
        BaseRepository (TwichStreamEntity): BaseRepository for TwichStreamRepository.
    """

    @abstractmethod
    def parse_stream(self, user_login: str) -> PublicParseStreamCalledEvent:
        """
        parse_stream: Return event about parsing twich stream.

        Args:
            user_login (str): Login of the user.

        Returns:
            PublicParseStreamCalledEvent: Event about parsing twich stream.
        """

        pass

    @abstractmethod
    def delete_stream_by_user_login(self, user_login: str) -> TwichStreamDeletedByUserLoginEvent:
        """
        delete_stream_by_user_login: Delete stream by user login.

        Args:
            user_login (str): Login of the user.

        Returns:
            TwichStreamDeletedByUserLoginEvent: Event about deleting twich stream.
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
