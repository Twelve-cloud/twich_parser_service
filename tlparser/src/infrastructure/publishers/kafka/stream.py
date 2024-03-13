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
from application.interfaces.publishers import ITwichStreamPublisher
from infrastructure.publishers.connections.kafka.producer import KafkaProducerConnection


class TwichStreamKafkaPublisher(ITwichStreamPublisher):
    def __init__(self, kafka_producer: KafkaProducerConnection) -> None:
        self.producer = kafka_producer.producer

    async def publish(self, events: list[TwichStreamDomainEvent]) -> None:
        for event in events:
            if isinstance(event, TwichStreamCreatedEvent):
                await self.publish_stream_created_event(event)
            elif isinstance(event, TwichStreamDeletedEvent):
                await self.publish_stream_deleted_event(event)

        return

    async def publish_stream_created_event(self, event: TwichStreamCreatedEvent) -> None:
        Thread(
            target=self.producer.send,
            args=(settings.KAFKA_STREAM_TOPIC, event),
            daemon=True,
        ).start()

    async def publish_stream_deleted_event(self, event: TwichStreamDeletedEvent) -> None:
        Thread(
            target=self.producer.send,
            args=(settings.KAFKA_STREAM_TOPIC, event),
            daemon=True,
        ).start()
