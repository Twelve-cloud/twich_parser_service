"""
products_service.py: File, containing lamoda products service abstract class.
"""


from abc import abstractmethod
from application.interfaces.services.base.base_service import IBaseService
from application.schemas.lamoda.product_schema import LamodaProductSchema


class ILamodaProductsService(IBaseService[LamodaProductSchema]):
    """
    ILamodaProductsService: Class, that represents abstract class for lamoda products service.

    Args:
        IBaseService (_type_): Base abstract class for lamoda products abstract class.
    """

    @abstractmethod
    async def parse_products(self, category: str) -> None:
        """
        parse_products: Called lamoda products publisher to publish event about parsing.

        Args:
            category (str): Category lamoda url.
        """

        pass

    @abstractmethod
    async def private_parse_products(self, category: str) -> list[LamodaProductSchema]:
        """
        private_parse_products: Parse lamoda products by category.

        Args:
            category (str): Category lamoda url.

        Returns:
            list[LamodaProductSchema]: List of LamodaProductSchema instances.
        """

        pass

    @abstractmethod
    async def delete_products_by_category(self, category: str) -> None:
        """
        delete_products_by_category: Delete products by category.

        Args:
            category (str): Category lamoda url.
        """

        pass

    @abstractmethod
    async def get_all_products(self) -> list[LamodaProductSchema]:
        """
        get_all_products: Return all products.

        Returns:
            list[LamodaProductSchema]: List of lamoda products.
        """

        pass

    @abstractmethod
    async def get_products_by_category(self, category: str) -> list[LamodaProductSchema]:
        """
        get_products_by_category: Return products by category.

        Args:
            category (str): Category lamoda url.

        Returns:
            list[LamodaProductSchema]: List of lamoda products with the same category.
        """

        pass
