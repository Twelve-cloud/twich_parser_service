"""
products_publisher.py: File, containing publisher abstract class for lamoda products.
"""


from abc import abstractmethod
from domain.events.lamoda.products_events import (
    LamodaProductCreatedOrUpdatedEvent,
    LamodaProductsDeletedByCategoryEvent,
    PublicParseProductsCalledEvent,
)
from domain.publishers.base.base_publisher import BasePublisher


class LamodaProductsPublisher(BasePublisher[LamodaProductCreatedOrUpdatedEvent]):
    """
    LamodaProductsPublisher: Abstract class for lamoda products publishers.

    Args:
        BasePublisher (_type_): Base publisher for LamodaProductsPublisher.
    """

    @abstractmethod
    def publish_parse_products_called_event(
        self,
        event: PublicParseProductsCalledEvent,
    ) -> None:
        """
        publish_parse_products_called_event: Publish public parse products called event.

        Args:
            event (PublicParseProductsCalledEvent): Public parse products called event.
        """

        pass

    @abstractmethod
    def publish_products_deleted_by_category_event(
        self,
        event: LamodaProductsDeletedByCategoryEvent,
    ) -> None:
        """
        publish_products_deleted_by_category_event: Publish products deleted by category event.

        Args:
            event (LamodaProductsDeletedByCategoryEvent): Lamoda products deleted by category event.
        """

        pass
