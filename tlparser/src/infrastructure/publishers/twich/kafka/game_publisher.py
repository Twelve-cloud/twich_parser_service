"""
game_publisher.py: File, containing kafka publisher class for twich game.
"""


from domain.events.twich.game_events import (
    PublicParseGameCalledEvent,
    TwichGameCreatedOrUpdatedEvent,
    TwichGameDeletedByNameEvent,
)
from domain.publishers.twich.game_publisher import TwichGamePublisher


class KafkaTwichGamePublisher(TwichGamePublisher):
    """
    KafkaTwichGamePublisher: Kafka implementation publisher class for twich game.

    Args:
        BasePublisher (_type_): Base publisher for KafkaTwichGamePublisher.
    """

    def publish_parse_game_called_event(
        self,
        event: PublicParseGameCalledEvent,
    ) -> None:
        """
        publish_parse_game_called_event: Publish public parse game called event.

        Args:
            event (PublicParseGameCalledEvent): Public parse game called event.
        """

        print('publish_parse_game_called_event')

    def publish_created_or_updated_event(
        self,
        event: TwichGameCreatedOrUpdatedEvent,
    ) -> None:
        """
        publish_created_or_updated_event: Publish game created/updated event.

        Args:
            event (TwichGameCreatedOrUpdatedEvent): Twich game created/updated event.
        """

        print('publish_created_or_updated_event')

    def publish_game_deleted_by_name_event(
        self,
        event: TwichGameDeletedByNameEvent,
    ) -> None:
        """
        publish_game_deleted_by_name_event: Publish game deleted by name event.

        Args:
            event (TwichGameDeletedByNameEvent): Twich game deleted by name event.
        """

        print('publish_game_deleted_by_name_event')
