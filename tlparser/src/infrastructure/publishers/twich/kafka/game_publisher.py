"""
game_publisher.py: File, containing kafka publisher class for twich game.
"""


from threading import Thread
from domain.events.twich.game_events import (
    PublicParseGameCalledEvent,
    TwichGameCreatedOrUpdatedEvent,
    TwichGameDeletedByNameEvent,
)
from domain.publishers.twich.game_publisher import TwichGamePublisher
from infrastructure.connections.kafka.producer import KafkaProducerConnection


class KafkaTwichGamePublisher(TwichGamePublisher):
    """
    KafkaTwichGamePublisher: Kafka implementation publisher class for twich game.

    Args:
        BasePublisher (_type_): Base publisher for KafkaTwichGamePublisher.
    """

    def __init__(self, kafka_producer: KafkaProducerConnection) -> None:
        """
        __init__: Initialize kafka twich game publisher.

        Args:
            kafka_producer (KafkaProducerConnection): Kafka producer connection.
        """

        self.producer = kafka_producer.producer

    def publish_parse_game_called_event(
        self,
        event: PublicParseGameCalledEvent,
    ) -> None:
        """
        publish_parse_game_called_event: Publish public parse game called event.

        Args:
            event (PublicParseGameCalledEvent): Public parse game called event.
        """

        Thread(target=self.producer.send, args=('parsing', event)).start()

    def publish_created_or_updated_event(
        self,
        event: TwichGameCreatedOrUpdatedEvent,
    ) -> None:
        """
        publish_created_or_updated_event: Publish game created/updated event.

        Args:
            event (TwichGameCreatedOrUpdatedEvent): Twich game created/updated event.
        """

        Thread(target=self.producer.send, args=('twich_game', event)).start()

    def publish_game_deleted_by_name_event(
        self,
        event: TwichGameDeletedByNameEvent,
    ) -> None:
        """
        publish_game_deleted_by_name_event: Publish game deleted by name event.

        Args:
            event (TwichGameDeletedByNameEvent): Twich game deleted by name event.
        """

        Thread(target=self.producer.send, args=('twich_game', event)).start()
