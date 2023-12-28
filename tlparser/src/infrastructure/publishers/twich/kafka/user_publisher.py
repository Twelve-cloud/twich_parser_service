"""
user_publisher.py: File, containing kafka publisher class for twich user.
"""


from threading import Thread
from common.config.base.settings import settings as base_settings
from common.config.twich.settings import settings as twich_settings
from domain.events.twich.user_events import (
    PublicParseUserCalledEvent,
    TwichUserCreatedOrUpdatedEvent,
    TwichUserDeletedByLoginEvent,
)
from domain.interfaces.publishers.twich.user_publisher import ITwichUserPublisher
from infrastructure.connections.kafka.producer import KafkaProducerConnection


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

    async def publish_parse_user_called_event(
        self,
        event: PublicParseUserCalledEvent,
    ) -> None:
        """
        publish_parse_user_called_event: Publish public parse user called event.

        Args:
            event (PublicParseUserCalledEvent): Public parse user called event.
        """

        Thread(target=self.producer.send, args=(base_settings.KAFKA_PARSING_TOPIC, event)).start()

    async def publish_created_or_updated_event(
        self,
        event: TwichUserCreatedOrUpdatedEvent,
    ) -> None:
        """
        publish_created_or_updated_event: Publish user created/updated event.

        Args:
            event (TwichUserCreatedOrUpdatedEvent): Twich user created/updated event.
        """

        Thread(target=self.producer.send, args=(twich_settings.KAFKA_USER_TOPIC, event)).start()

    async def publish_user_deleted_by_login_event(
        self,
        event: TwichUserDeletedByLoginEvent,
    ) -> None:
        """
        publish_user_deleted_by_login_event: Publish user deleted by login event.

        Args:
            event (TwichUserDeletedByLoginEvent): Twich user deleted by login event.
        """

        Thread(target=self.producer.send, args=(twich_settings.KAFKA_USER_TOPIC, event)).start()
