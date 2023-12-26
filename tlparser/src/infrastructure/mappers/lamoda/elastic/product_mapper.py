"""
product_mapper.py: File, containig lamoda product mapper.
"""


from domain.entities.lamoda.product_entity import LamodaProductEntity
from infrastructure.models.lamoda.elastic.product_model import LamodaProduct


class LamodaProductMapper:
    """
    LamodaProductMapper: Class, representing lamoda product mapper.
    """

    @classmethod
    def to_domain(self, persistence: LamodaProduct) -> LamodaProductEntity:
        """
        to_domain: Transform persistence product model to domain product model.

        Args:
            persistence (LamodaProduct): Persistence product model.

        Returns:
            LamodaProductEntity: Domain product model.
        """

        return LamodaProductEntity(
            sku=persistence.sku,
            url=persistence.url,
            category=persistence.category,
            description=persistence.description,
            price=persistence.price,
            price_currency=persistence.price_currency,
            price_valid_until=persistence.price_valid_until,
            parsed_at=persistence.parsed_at,
        )

    @classmethod
    def to_persistence(self, domain: LamodaProductEntity) -> LamodaProduct:
        """
        to_persistence: Transform domain product model to persistence product model.

        Args:
            domain (LamodaProductEntity): Domain product model.

        Returns:
            LamodaProduct: Persistence product model.
        """

        return LamodaProduct(
            sku=domain.sku,
            url=domain.url,
            category=domain.category,
            description=domain.category,
            price=domain.price,
            price_currency=domain.price_currency,
            price_valid_until=domain.price_valid_until,
            parsed_at=domain.parsed_at,
        )
