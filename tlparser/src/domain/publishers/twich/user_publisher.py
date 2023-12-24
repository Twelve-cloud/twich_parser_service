"""
user_publisher.py: File, containing publisher abstract class for twich user.
"""


from abc import abstractmethod
from domain.events.twich.user_events import (
    PublicParseUserCalledEvent,
    TwichUserCreatedOrUpdatedEvent,
    TwichUserDeletedByLoginEvent,
)
from domain.publishers.base.base_publisher import BasePublisher


class TwichUserPublisher(BasePublisher[TwichUserCreatedOrUpdatedEvent]):
    """
    TwichUserPublisher: Abstract class for twich user publishers.

    Args:
        BasePublisher (TwichUserCreatedOrUpdatedEvent): Base publisher for TwichUserPublisher.
    """

    @abstractmethod
    def publish_parse_user_called_event(
        self,
        event: PublicParseUserCalledEvent,
    ) -> None:
        """
        publish_parse_user_called_event: Publish public parse user called event.

        Args:
            event (PublicParseUserCalledEvent): Public parse user called event.
        """

        pass

    @abstractmethod
    def publish_user_deleted_by_login_event(
        self,
        event: TwichUserDeletedByLoginEvent,
    ) -> None:
        """
        publish_user_deleted_by_login_event: Publish user deleted by login event.

        Args:
            event (TwichUserDeletedByLoginEvent): Twich user deleted by login event.
        """

        pass
