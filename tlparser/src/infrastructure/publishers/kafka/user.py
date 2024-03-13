"""
user_publisher.py: File, containing kafka publisher class for twich user.
"""


from threading import Thread
from common.config import settings
from domain.events.user import (
    TwichUserCreatedEvent,
    TwichUserDeletedEvent,
    TwichUserDomainEvent,
)
from application.interfaces.publishers import ITwichUserPublisher
from infrastructure.publishers.connections.kafka.producer import KafkaProducerConnection


class TwichUserKafkaPublisher(ITwichUserPublisher):
    def __init__(self, kafka_producer: KafkaProducerConnection) -> None:
        self.producer = kafka_producer.producer

    async def publish(self, events: list[TwichUserDomainEvent]) -> None:
        for event in events:
            if isinstance(event, TwichUserCreatedEvent):
                await self.publish_user_created_event(event)
            elif isinstance(event, TwichUserDeletedEvent):
                await self.publish_user_deleted_event(event)

        return

    async def publish_user_created_event(self, event: TwichUserCreatedEvent) -> None:
        Thread(
            target=self.producer.send,
            args=(settings.KAFKA_USER_TOPIC, event),
            daemon=True,
        ).start()

    async def publish_user_deleted_event(self, event: TwichUserDeletedEvent) -> None:
        Thread(
            target=self.producer.send,
            args=(settings.KAFKA_USER_TOPIC, event),
            daemon=True,
        ).start()
