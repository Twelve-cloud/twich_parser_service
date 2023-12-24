"""
products_publisher.py: File, containing kafka publisher class for lamoda products.
"""


from domain.events.lamoda.products_events import (
    LamodaProductCreatedOrUpdatedEvent,
    LamodaProductsDeletedByCategoryEvent,
    PublicParseProductsCalledEvent,
)
from domain.publishers.lamoda.products_publisher import LamodaProductsPublisher


class KafkaLamodaProductsPublisher(LamodaProductsPublisher):
    """
    KafkaLamodaProductsPublisher: Kafka implementation publisher class for lamoda products.

    Args:
        BasePublisher (_type_): Base publisher for KafkaLamodaProductsPublisher.
    """

    def publish_parse_products_called_event(
        self,
        event: PublicParseProductsCalledEvent,
    ) -> None:
        """
        publish_parse_products_called_event: Publish public parse products called event.

        Args:
            event (PublicParseProductsCalledEvent): Public parse products called event.
        """

        print('publish_parse_products_called_event')

    def publish_created_or_updated_event(
        self,
        event: LamodaProductCreatedOrUpdatedEvent,
    ) -> None:
        """
        publish_created_or_updated_event: Publish products created/updated event.

        Args:
            event (LamodaProductCreatedOrUpdatedEvent): Lamoda products created/updated event.
        """

        print('publish_created_or_updated_event')

    def publish_products_deleted_by_category_event(
        self,
        event: LamodaProductsDeletedByCategoryEvent,
    ) -> None:
        """
        publish_products_deleted_by_category_event: Publish products deleted by category event.

        Args:
            event (LamodaProductsDeletedByCategoryEvent): Lamoda products deleted by category event.
        """

        print('publish_products_deleted_by_category_event')
