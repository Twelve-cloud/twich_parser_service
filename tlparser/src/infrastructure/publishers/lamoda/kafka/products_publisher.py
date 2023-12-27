"""
products_publisher.py: File, containing kafka publisher class for lamoda products.
"""


from threading import Thread
from common.config.base.settings import settings as base_settings
from common.config.lamoda.settings import settings as lamoda_settings
from domain.events.lamoda.products_events import (
    LamodaProductCreatedOrUpdatedEvent,
    LamodaProductsDeletedByCategoryEvent,
    PublicParseProductsCalledEvent,
)
from domain.publishers.lamoda.products_publisher import ILamodaProductsPublisher
from infrastructure.connections.kafka.producer import KafkaProducerConnection


class LamodaProductsKafkaPublisher(ILamodaProductsPublisher):
    """
    LamodaProductsKafkaPublisher: Kafka implementation publisher class for lamoda products.

    Args:
        IBasePublisher (_type_): Base publisher for LamodaProductsKafkaPublisher.
    """

    def __init__(self, kafka_producer: KafkaProducerConnection) -> None:
        """
        __init__: Initialize kafka twich game publisher.

        Args:
            kafka_producer (KafkaProducerConnection): Kafka producer connection.
        """

        self.producer = kafka_producer.producer

    def publish_parse_products_called_event(
        self,
        event: PublicParseProductsCalledEvent,
    ) -> None:
        """
        publish_parse_products_called_event: Publish public parse products called event.

        Args:
            event (PublicParseProductsCalledEvent): Public parse products called event.
        """

        Thread(target=self.producer.send, args=(base_settings.KAFKA_PARSING_TOPIC, event)).start()

    def publish_created_or_updated_event(
        self,
        event: LamodaProductCreatedOrUpdatedEvent,
    ) -> None:
        """
        publish_created_or_updated_event: Publish products created/updated event.

        Args:
            event (LamodaProductCreatedOrUpdatedEvent): Lamoda products created/updated event.
        """

        Thread(target=self.producer.send, args=(lamoda_settings.KAFKA_PRODUCT_TOPIC, event)).start()

    def publish_products_deleted_by_category_event(
        self,
        event: LamodaProductsDeletedByCategoryEvent,
    ) -> None:
        """
        publish_products_deleted_by_category_event: Publish products deleted by category event.

        Args:
            event (LamodaProductsDeletedByCategoryEvent): Lamoda products deleted by category event.
        """

        Thread(target=self.producer.send, args=(lamoda_settings.KAFKA_PRODUCT_TOPIC, event)).start()
