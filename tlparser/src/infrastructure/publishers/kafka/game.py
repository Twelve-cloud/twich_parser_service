"""
game_publisher.py: File, containing kafka publisher class for twich game.
"""


from threading import Thread
from common.config.base.settings import settings as base_settings
from common.config.twich.settings import settings as twich_settings
from domain.events.game import (
    PublicParseGameCalledEvent,
    TwichGameCreatedOrUpdatedEvent,
    TwichGameDeletedByNameEvent,
)
from domain.interfaces.publishers.base import E
from domain.exceptions.publishers.game import ITwichGamePublisher
from infrastructure.connections.kafka.producer import KafkaProducerConnection


class TwichGameKafkaPublisher(ITwichGamePublisher):
    """
    TwichGameKafkaPublisher: Kafka implementation publisher class for twich game.

    Args:
        IBasePublisher (_type_): Base publisher for TwichGameKafkaPublisher.
    """

    def __init__(self, kafka_producer: KafkaProducerConnection) -> None:
        """
        __init__: Initialize kafka twich game publisher.

        Args:
            kafka_producer (KafkaProducerConnection): Kafka producer connection.
        """

        self.producer = kafka_producer.producer

    async def publish(self, events: list[E]) -> None:
        """
        publish: Call handlers for every event.

        Args:
            events (list[E]): List of events.
        """

        for event in events:
            if isinstance(event, PublicParseGameCalledEvent):
                await self.publish_parse_game_called_event(event)
            elif isinstance(event, TwichGameCreatedOrUpdatedEvent):
                await self.publish_created_or_updated_event(event)
            elif isinstance(event, TwichGameDeletedByNameEvent):
                await self.publish_game_deleted_by_name_event(event)

        return

    async def publish_parse_game_called_event(
        self,
        event: PublicParseGameCalledEvent,
    ) -> None:
        """
        publish_parse_game_called_event: Publish public parse game called event.

        Args:
            event (PublicParseGameCalledEvent): Public parse game called event.
        """

        Thread(
            target=self.producer.send,
            args=(base_settings.KAFKA_PARSING_TOPIC, event),
            daemon=True,
        ).start()

    async def publish_created_or_updated_event(
        self,
        event: TwichGameCreatedOrUpdatedEvent,
    ) -> None:
        """
        publish_created_or_updated_event: Publish game created/updated event.

        Args:
            event (TwichGameCreatedOrUpdatedEvent): Twich game created/updated event.
        """

        Thread(
            target=self.producer.send,
            args=(twich_settings.KAFKA_GAME_TOPIC, event),
            daemon=True,
        ).start()

    async def publish_game_deleted_by_name_event(
        self,
        event: TwichGameDeletedByNameEvent,
    ) -> None:
        """
        publish_game_deleted_by_name_event: Publish game deleted by name event.

        Args:
            event (TwichGameDeletedByNameEvent): Twich game deleted by name event.
        """

        Thread(
            target=self.producer.send,
            args=(twich_settings.KAFKA_GAME_TOPIC, event),
            daemon=True,
        ).start()
