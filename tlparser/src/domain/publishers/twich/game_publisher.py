"""
game_publisher.py: File, containing publisher abstract class for twich game.
"""


from abc import abstractmethod
from domain.events.twich.game_events import (
    PublicParseGameCalledEvent,
    TwichGameCreatedOrUpdatedEvent,
    TwichGameDeletedByNameEvent,
)
from domain.publishers.base.base_publisher import BasePublisher


class TwichGamePublisher(BasePublisher[TwichGameCreatedOrUpdatedEvent]):
    """
    TwichGamePublisher: Abstract class for twich game publishers.

    Args:
        BasePublisher (TwichGameCreatedOrUpdatedEvent): Base publisher for TwichGamePublisher.
    """

    @abstractmethod
    def publish_parse_game_called_event(
        self,
        event: PublicParseGameCalledEvent,
    ) -> None:
        """
        publish_parse_game_called_event: Publish public parse game called event.

        Args:
            event (PublicParseGameCalledEvent): Public parse game called event.
        """

        pass

    @abstractmethod
    def publish_game_deleted_by_name_event(
        self,
        event: TwichGameDeletedByNameEvent,
    ) -> None:
        """
        publish_game_deleted_by_name_event: Publish game deleted by name event.

        Args:
            event (TwichGameDeletedByNameEvent): Twich game deleted by name event.
        """

        pass
