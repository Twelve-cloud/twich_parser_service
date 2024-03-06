"""
game.py: File, containing publisher interface for a twich user.
"""


from abc import abstractmethod
from domain.events import (
    TwichUserCreatedEvent,
    TwichUserDeletedEvent,
    TwichUserDomainEvent,
)
from domain.interfaces.publishers import IBasePublisher


class ITwichUserPublisher(IBasePublisher[TwichUserDomainEvent]):
    """
    ITwichUserPublisher: Class that represents publisher interface for a twich user.

    Args:
        IBasePublisher: Base publisher interface instantiated with twich user domain event.
    """

    @abstractmethod
    async def publish_user_created_event(self, event: TwichUserCreatedEvent) -> None:
        """
        publish_user_created_event: Should publish event that user is created.
        Must be overriden.

        Args:
            event (TwichUserCreatedEvent): Twich user domain event.
                That domain event represents that twich user has been created.
        """

        pass

    @abstractmethod
    async def publish_user_deleted_event(self, event: TwichUserDeletedEvent) -> None:
        """
        publish_user_deleted_event: Should publish event that user is deleted.
        Must be overriden.

        Args:
            event (TwichUserDeletedEvent): Twich user domain event.
                That domain event represents that twich user has been deleted.
        """

        pass
