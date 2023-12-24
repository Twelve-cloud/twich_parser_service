"""
stream_publisher.py: File, containing kafka publisher class for twich stream.
"""


from domain.events.twich.stream_events import (
    PublicParseStreamCalledEvent,
    TwichStreamCreatedOrUpdatedEvent,
    TwichStreamDeletedByUserLoginEvent,
)
from domain.publishers.twich.stream_publisher import TwichStreamPublisher


class KafkaTwichStreamPublisher(TwichStreamPublisher):
    """
    KafkaTwichStreamPublisher: Kafka implementation publisher class for twich stream.

    Args:
        BasePublisher (_type_): Base publisher for KafkaTwichStreamPublisher.
    """

    def publish_parse_stream_called_event(
        self,
        event: PublicParseStreamCalledEvent,
    ) -> None:
        """
        publish_parse_stream_called_event: Publish public parse stream called event.

        Args:
            event (PublicParseStreamCalledEvent): Public parse stream called event.
        """

        print('publish_parse_stream_called_event')

    def publish_created_or_updated_event(
        self,
        event: TwichStreamCreatedOrUpdatedEvent,
    ) -> None:
        """
        publish_created_or_updated_event: Publish stream created/updated event.

        Args:
            event (TwichStreamCreatedOrUpdatedEvent): Twich stream created/updated event.
        """

        print('publish_created_or_updated_event')

    def publish_stream_deleted_by_user_login_event(
        self,
        event: TwichStreamDeletedByUserLoginEvent,
    ) -> None:
        """
        publish_stream_deleted_by_user_login_event: Publish stream deleted by user login event.

        Args:
            event (TwichStreamDeletedByUserLoginEvent): Twich stream deleted by user login event.
        """

        print('publish_stream_deleted_by_user_login_event')
