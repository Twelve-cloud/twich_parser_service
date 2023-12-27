"""
game_publisher.py: File, containing kafka publisher class for twich game.
"""


from threading import Thread
from common.config.base.settings import settings as base_settings
from common.config.twich.settings import settings as twich_settings
from domain.events.twich.game_events import (
    PublicParseGameCalledEvent,
    TwichGameCreatedOrUpdatedEvent,
    TwichGameDeletedByNameEvent,
)
from domain.publishers.twich.game_publisher import TwichGamePublisher
from infrastructure.connections.kafka.producer import KafkaProducerConnection


class TwichGameKafkaPublisher(TwichGamePublisher):
    """
    TwichGameKafkaPublisher: Kafka implementation publisher class for twich game.

    Args:
        BasePublisher (_type_): Base publisher for TwichGameKafkaPublisher.
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

        Thread(target=self.producer.send, args=(base_settings.KAFKA_PARSING_TOPIC, event)).start()

    def publish_created_or_updated_event(
        self,
        event: TwichGameCreatedOrUpdatedEvent,
    ) -> None:
        """
        publish_created_or_updated_event: Publish game created/updated event.

        Args:
            event (TwichGameCreatedOrUpdatedEvent): Twich game created/updated event.
        """

        Thread(target=self.producer.send, args=(twich_settings.KAFKA_GAME_TOPIC, event)).start()

    def publish_game_deleted_by_name_event(
        self,
        event: TwichGameDeletedByNameEvent,
    ) -> None:
        """
        publish_game_deleted_by_name_event: Publish game deleted by name event.

        Args:
            event (TwichGameDeletedByNameEvent): Twich game deleted by name event.
        """

        Thread(target=self.producer.send, args=(twich_settings.KAFKA_GAME_TOPIC, event)).start()
