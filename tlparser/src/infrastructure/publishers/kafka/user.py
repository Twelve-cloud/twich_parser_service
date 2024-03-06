"""
user_publisher.py: File, containing kafka publisher class for twich user.
"""


from threading import Thread
from common.config import settings
from domain.events.user import (
    TwichUserCreatedEvent,
    TwichUserDeletedByLoginEvent,
    TwichUserDomainEvent,
)
from domain.interfaces.publishers import ITwichUserPublisher
from infrastructure.publishers.connections.kafka.producer import KafkaProducerConnection


class TwichUserKafkaPublisher(ITwichUserPublisher):
    """
    TwichUserKafkaPublisher: Kafka implementation publisher class for twich user.

    Args:
        IBasePublisher (_type_): Base publisher for TwichUserKafkaPublisher.
    """

    def __init__(self, kafka_producer: KafkaProducerConnection) -> None:
        """
        __init__: Initialize kafka twich game publisher.

        Args:
            kafka_producer (KafkaProducerConnection): Kafka producer connection.
        """

        self.producer = kafka_producer.producer

    async def publish(self, events: list[TwichUserDomainEvent]) -> None:
        """
        publish: Call handlers for every event.

        Args:
            events (list[E]): List of events.
        """

        for event in events:
            if isinstance(event, TwichUserCreatedEvent):
                await self.publish_user_created_event(event)
            elif isinstance(event, TwichUserDeletedByLoginEvent):
                await self.publish_user_deleted_by_login_event(event)

        return

    async def publish_user_created_event(
        self,
        event: TwichUserCreatedEvent,
    ) -> None:
        """
        publish_created_or_updated_event: Publish user created/updated event.

        Args:
            event (TwichUserCreatedOrUpdatedEvent): Twich user created/updated event.
        """

        Thread(
            target=self.producer.send,
            args=(settings.KAFKA_USER_TOPIC, event),
            daemon=True,
        ).start()

    async def publish_user_deleted_by_login_event(
        self,
        event: TwichUserDeletedByLoginEvent,
    ) -> None:
        """
        publish_user_deleted_by_login_event: Publish user deleted by login event.

        Args:
            event (TwichUserDeletedByLoginEvent): Twich user deleted by login event.
        """

        Thread(
            target=self.producer.send,
            args=(settings.KAFKA_USER_TOPIC, event),
            daemon=True,
        ).start()
