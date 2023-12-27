"""
product_mapper.py: File, containing mapper for lamoda product.
"""


from domain.entities.lamoda.product_entity import LamodaProductEntity
from presentation.schemas.lamoda.product_schema import LamodaProductSchema


class LamodaProductMapper:
    """
    LamodaProductMapper: Class, that transform product schema to product domain model and vv.
    """

    @classmethod
    def to_domain(cls, schema: LamodaProductSchema) -> LamodaProductEntity:
        """
        to_domain: Transform lamoda product read schema to lamoda product domain model.

        Args:
            schema (LamodaProductSchema): Lamoda product read schema instance.

        Returns:
            LamodaProductEntity: Lamoda domain model instance.
        """

        return LamodaProductEntity(**schema.model_dump())

    @classmethod
    def to_schema(cls, domain: LamodaProductEntity) -> LamodaProductSchema:
        """
        to_schema: Transform lamoda product domain model to lamoda product read schema.

        Args:
            domain (LamodaProductEntity): Lamoda product domain model instance.

        Returns:
            LamodaProductSchema: Lamoda product read schema instance.
        """

        return LamodaProductSchema.model_construct(
            sku=domain.sku,
            url=domain.url,
            category=domain.category,
            description=domain.description,
            price=domain.price,
            price_currency=domain.price_currency,
            price_valid_until=domain.price_valid_until,
            parsed_at=domain.parsed_at,
        )
