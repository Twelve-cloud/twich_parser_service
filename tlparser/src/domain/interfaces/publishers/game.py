"""
game.py: File, containing publisher interface for a twich game.
"""


from abc import abstractmethod
from domain.events import (
    TwichGameCreatedEvent,
    TwichGameDeletedByNameEvent,
    TwichGameDomainEvent,
)
from domain.interfaces.publishers import IBasePublisher


class ITwichGamePublisher(IBasePublisher[TwichGameDomainEvent]):
    """
    ITwichGamePublisher: Class that represents publisher interface for a twich game.

    Args:
        IBasePublisher: Base publisher interface instantiated with twich game domain event.
    """

    @abstractmethod
    async def publish_game_created_event(
        self,
        event: TwichGameCreatedEvent,
    ) -> None:
        """
        publish_game_created_event: Should publish event that game is created.
        Must be overriden.

        Args:
            event (TwichGameCreatedEvent): Twich game domain event.
                That domain event represents that twich game has been created.
        """

        pass

    @abstractmethod
    async def publish_game_deleted_by_name_event(
        self,
        event: TwichGameDeletedByNameEvent,
    ) -> None:
        """
        publish_game_deleted_by_name_event: Should publish event that game is deleted.
        Must be overriden.

        Args:
            event (TwichGameDeletedByNameEvent): Twich game domain event.
                That domain event represents that twich game has been deleted by name.
        """

        pass
