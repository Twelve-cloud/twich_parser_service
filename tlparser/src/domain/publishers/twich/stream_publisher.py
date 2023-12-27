"""
stream_publisher.py: File, containing publisher abstract class for twich stream.
"""


from abc import abstractmethod
from domain.events.twich.stream_events import (
    PublicParseStreamCalledEvent,
    TwichStreamCreatedOrUpdatedEvent,
    TwichStreamDeletedByUserLoginEvent,
)
from domain.publishers.base.base_publisher import IBasePublisher


class ITwichStreamPublisher(IBasePublisher[TwichStreamCreatedOrUpdatedEvent]):
    """
    ITwichStreamPublisher: Abstract class for twich stream publishers.

    Args:
        IBasePublisher (TwichStreamCreatedOrUpdatedEvent): Base publisher for ITwichStreamPublisher.
    """

    @abstractmethod
    def publish_parse_stream_called_event(
        self,
        event: PublicParseStreamCalledEvent,
    ) -> None:
        """
        publish_parse_stream_called_event: Publish public parse stream called event.

        Args:
            event (PublicParseStreamCalledEvent): Public parse stream called event.
        """

        pass

    @abstractmethod
    def publish_stream_deleted_by_user_login_event(
        self,
        event: TwichStreamDeletedByUserLoginEvent,
    ) -> None:
        """
        publish_stream_deleted_by_user_login_event: Publish stream deleted by user login event.

        Args:
            event (TwichStreamDeletedByUserLoginEvent): Twich stream deleted by user login event.
        """

        pass
