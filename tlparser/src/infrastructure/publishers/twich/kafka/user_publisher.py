"""
user_publisher.py: File, containing kafka publisher class for twich user.
"""


from threading import Thread
from domain.events.twich.user_events import (
    PublicParseUserCalledEvent,
    TwichUserCreatedOrUpdatedEvent,
    TwichUserDeletedByLoginEvent,
)
from domain.publishers.twich.user_publisher import TwichUserPublisher
from infrastructure.connections.kafka.producer import KafkaProducerConnection


class KafkaTwichUserPublisher(TwichUserPublisher):
    """
    KafkaTwichUserPublisher: Kafka implementation publisher class for twich user.

    Args:
        BasePublisher (_type_): Base publisher for KafkaTwichUserPublisher.
    """

    def __init__(self, kafka_producer: KafkaProducerConnection) -> None:
        """
        __init__: Initialize kafka twich game publisher.

        Args:
            kafka_producer (KafkaProducerConnection): Kafka producer connection.
        """

        self.producer = kafka_producer.producer

    def publish_parse_user_called_event(
        self,
        event: PublicParseUserCalledEvent,
    ) -> None:
        """
        publish_parse_user_called_event: Publish public parse user called event.

        Args:
            event (PublicParseUserCalledEvent): Public parse user called event.
        """

        Thread(target=self.producer.send, args=('parsing', event)).start()

    def publish_created_or_updated_event(
        self,
        event: TwichUserCreatedOrUpdatedEvent,
    ) -> None:
        """
        publish_created_or_updated_event: Publish user created/updated event.

        Args:
            event (TwichUserCreatedOrUpdatedEvent): Twich user created/updated event.
        """

        Thread(target=self.producer.send, args=('twich_user', event)).start()

    def publish_user_deleted_by_login_event(
        self,
        event: TwichUserDeletedByLoginEvent,
    ) -> None:
        """
        publish_user_deleted_by_login_event: Publish user deleted by login event.

        Args:
            event (TwichUserDeletedByLoginEvent): Twich user deleted by login event.
        """

        Thread(target=self.producer.send, args=('twich_user', event)).start()
