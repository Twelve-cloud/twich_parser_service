"""
products_repository.py: File, containing repository abstract class for lamoda products.
"""


from abc import abstractmethod
from domain.entities.lamoda.product_entity import LamodaProductEntity
from domain.repositories.base.base_repository import BaseRepository


class LamodaProductsRepository(BaseRepository[LamodaProductEntity]):
    """
    LamodaProductsRepository: Abstract class for lamoda products repositories.

    Args:
        BaseRepository (LamodaProductEntity): BaseRepository for LamodaProductsRepository.
    """

    def delete_products_by_category(self, category: str) -> None:
        """
        delete_products_by_category: Delete products by category.

        Args:
            category (str): Products category.
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
