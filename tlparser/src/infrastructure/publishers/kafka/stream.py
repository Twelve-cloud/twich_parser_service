"""
stream_publisher.py: File, containing kafka publisher class for twich stream.
"""


from threading import Thread
from common.config import settings
from domain.events.stream import (
    TwichStreamCreatedEvent,
    TwichStreamDeletedEvent,
    TwichStreamDomainEvent,
)
from domain.interfaces.publishers import ITwichStreamPublisher
from infrastructure.publishers.connections.kafka.producer import KafkaProducerConnection


class TwichStreamKafkaPublisher(ITwichStreamPublisher):
    """
    TwichStreamKafkaPublisher: Kafka implementation publisher class for twich stream.

    Args:
        IBasePublisher: Base publisher for TwichStreamKafkaPublisher.
    """

    def __init__(self, kafka_producer: KafkaProducerConnection) -> None:
        """
        __init__: Initialize kafka twich game publisher.

        Args:
            kafka_producer (KafkaProducerConnection): Kafka producer connection.
        """

        self.producer = kafka_producer.producer

    async def publish(self, events: list[TwichStreamDomainEvent]) -> None:
        """
        publish: Call handlers for every event.

        Args:
            events (list[E]): List of events.
        """

        for event in events:
            if isinstance(event, TwichStreamCreatedEvent):
                await self.publish_stream_created_event(event)
            elif isinstance(event, TwichStreamDeletedEvent):
                await self.publish_stream_deleted_event(event)

        return

    async def publish_stream_created_event(self, event: TwichStreamCreatedEvent) -> None:
        """
        publish_created_event: Publish stream created event.

        Args:
            event (TwichStreamCreatedEvent): Twich stream created event.
        """

        Thread(
            target=self.producer.send,
            args=(settings.KAFKA_STREAM_TOPIC, event),
            daemon=True,
        ).start()

    async def publish_stream_deleted_event(self, event: TwichStreamDeletedEvent) -> None:
        """
        publish_stream_deleted_event: Publish stream deleted  event.

        Args:
            event (TwichStreamDeletedEvent): Twich stream deleted event.
        """

        Thread(
            target=self.producer.send,
            args=(settings.KAFKA_STREAM_TOPIC, event),
            daemon=True,
        ).start()
