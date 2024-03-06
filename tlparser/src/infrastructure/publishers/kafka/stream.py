"""
stream_publisher.py: File, containing kafka publisher class for twich stream.
"""


from threading import Thread
from common.config import settings
from domain.events.stream import (
    TwichStreamCreatedEvent,
    TwichStreamDeletedByUserLoginEvent,
    TwichStreamDomainEvent,
)
from domain.interfaces.publishers import ITwichStreamPublisher
from infrastructure.publishers.connections.kafka.producer import KafkaProducerConnection


class TwichStreamKafkaPublisher(ITwichStreamPublisher):
    """
    TwichStreamKafkaPublisher: Kafka implementation publisher class for twich stream.

    Args:
        IBasePublisher (_type_): Base publisher for TwichStreamKafkaPublisher.
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
            elif isinstance(event, TwichStreamDeletedByUserLoginEvent):
                await self.publish_stream_deleted_by_user_login_event(event)

        return

    async def publish_stream_created_event(
        self,
        event: TwichStreamCreatedEvent,
    ) -> None:
        """
        publish_created_or_updated_event: Publish stream created/updated event.

        Args:
            event (TwichStreamCreatedOrUpdatedEvent): Twich stream created/updated event.
        """

        Thread(
            target=self.producer.send,
            args=(settings.KAFKA_STREAM_TOPIC, event),
            daemon=True,
        ).start()

    async def publish_stream_deleted_by_user_login_event(
        self,
        event: TwichStreamDeletedByUserLoginEvent,
    ) -> None:
        """
        publish_stream_deleted_by_user_login_event: Publish stream deleted by user login event.

        Args:
            event (TwichStreamDeletedByUserLoginEvent): Twich stream deleted by user login event.
        """

        Thread(
            target=self.producer.send,
            args=(settings.KAFKA_STREAM_TOPIC, event),
            daemon=True,
        ).start()
