"""
stream.py: File, containing publisher interface for a twich stream.
"""


from abc import abstractmethod
from domain.events import (
    TwichStreamCreatedEvent,
    TwichStreamDeletedEvent,
    TwichStreamDomainEvent,
)
from domain.interfaces.publishers import IBasePublisher


class ITwichStreamPublisher(IBasePublisher[TwichStreamDomainEvent]):
    """
    ITwichStreamPublisher: Class that represents publisher interface for a twich stream.

    Args:
        IBasePublisher: Base publisher interface instantiated with twich stream domain event.
    """

    @abstractmethod
    async def publish_stream_created_event(self, event: TwichStreamCreatedEvent) -> None:
        """
        publish_stream_created_event: Should publish event that stream is created.
        Must be overriden.

        Args:
            event (TwichStreamCreatedEvent): Twich stream domain event.
                That domain event represents that twich stream has been created.
        """

        pass

    @abstractmethod
    async def publish_stream_deleted_event(self, event: TwichStreamDeletedEvent) -> None:
        """
        publish_stream_deleted_event: Should publish event that stream is deleted.
        Must be overriden.

        Args:
            event (TwichStreamDeletedEvent): Twich stream domain event.
                That domain event represents that twich stream has been deleted.
        """

        pass
