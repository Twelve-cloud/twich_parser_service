"""
stream_publisher.py: File, containing kafka publisher class for twich stream.
"""


from threading import Thread

from application.interfaces.publisher import ITwichStreamPublisher
from domain.events.stream import (
    TwichStreamCreated,
    TwichStreamDeleted,
    TwichStreamDomainEvent,
)
from infrastructure.publishers.connections.kafka.producer import KafkaProducerConnection
from shared.config import settings


class TwichStreamKafkaPublisher(ITwichStreamPublisher):
    def __init__(self, kafka_producer: KafkaProducerConnection) -> None:
        self.producer = kafka_producer.producer

    async def publish(self, events: list[TwichStreamDomainEvent]) -> None:
        for event in events:
            if isinstance(event, TwichStreamCreated):
                await self.publish_stream_created_event(event)
            elif isinstance(event, TwichStreamDeleted):
                await self.publish_stream_deleted_event(event)

        return

    async def publish_stream_created_event(self, event: TwichStreamCreated) -> None:
        Thread(
            target=self.producer.send,
            args=(settings.KAFKA_STREAM_TOPIC, event),
            daemon=True,
        ).start()

    async def publish_stream_deleted_event(self, event: TwichStreamDeleted) -> None:
        Thread(
            target=self.producer.send,
            args=(settings.KAFKA_STREAM_TOPIC, event),
            daemon=True,
        ).start()
