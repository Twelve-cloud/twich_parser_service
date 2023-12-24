"""
products_repository.py: File, containing repository abstract class for lamoda products.
"""


from abc import abstractmethod
from domain.entities.lamoda.product_entity import LamodaProductEntity
from domain.events.lamoda.products_events import (
    LamodaProductCreatedOrUpdatedEvent,
    LamodaProductsDeletedByCategoryEvent,
    PublicParseProductsCalledEvent,
)
from domain.repositories.base.base_repository import BaseRepository


class LamodaProductsRepository(
    BaseRepository[LamodaProductEntity, LamodaProductCreatedOrUpdatedEvent]
):
    """
    LamodaProductsRepository: Abstract class for lamoda products repositories.

    Args:
        BaseRepository (LamodaProductEntity): BaseRepository for LamodaProductsRepository.
    """

    @abstractmethod
    def parse_products(self, category: str) -> PublicParseProductsCalledEvent:
        """
        parse_products: Return event about parsing products.

        Args:
            category (str): Products category.

        Returns:
            PublicParseProductsCalledEvent: Event about parsing products.
        """

        pass

    @abstractmethod
    def delete_products_by_category(self, category: str) -> LamodaProductsDeletedByCategoryEvent:
        """
        delete_products_by_category: Delete products by category.

        Args:
            category (str): Products category.

        Returns:
            LamodaProductsDeletedByCategoryEvent: Event about deleting products.
        """

        pass

    @abstractmethod
    def get_products_by_category(self, category: str) -> list[LamodaProductEntity]:
        """
        get_products_by_category: Return products by category.

        Args:
            category (str): Products category.

        Returns:
            list[LamodaProductEntity]: List of lamoda products entities with the same category.
        """

        pass
