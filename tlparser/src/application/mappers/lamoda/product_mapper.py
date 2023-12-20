"""
product_mapper.py: File, containing mapper for lamoda product.
"""


from application.schemas.lamoda.product_schema import (
    LamodaProductCreateSchema,
    LamodaProductReadSchema,
)
from domain.entities.lamoda.product_entity import LamodaProductEntity


class LamodaProductCreateMapper:
    """
    LamodaProductCreateMapper: Class, that transform product schema to product domain model and vv.
    """

    @classmethod
    def to_domain(cls, schema: LamodaProductCreateSchema) -> LamodaProductEntity:
        """
        to_domain: Transform lamoda product create schema to lamoda product domain model.

        Args:
            schema (LamodaProductCreateSchema): Lamoda product create schema instance.

        Returns:
            LamodaProductEntity: Lamoda domain model instance.
        """

        return LamodaProductEntity(**schema.model_dump())

    @classmethod
    def to_schema(cls, domain: LamodaProductEntity) -> LamodaProductCreateSchema:
        """
        to_schema: Transform lamoda product domain model to lamoda product create schema.

        Args:
            domain (LamodaProductEntity): Lamoda product domain model instance.

        Returns:
            LamodaProductCreateSchema: Lamoda product create schema instance.
        """

        return LamodaProductCreateSchema.model_construct(
            sku=domain.sku,
            url=domain.url,
            category=domain.category,
            description=domain.description,
            price=domain.price,
            price_currency=domain.price_currency,
            price_valid_until=domain.price_valid_until,
        )


class LamodaProductReadMapper:
    """
    LamodaProductReadMapper: Class, that transform product schema to product domain model and vv.
    """

    @classmethod
    def to_domain(cls, schema: LamodaProductReadSchema) -> LamodaProductEntity:
        """
        to_domain: Transform lamoda product read schema to lamoda product domain model.

        Args:
            schema (LamodaProductReadSchema): Lamoda product read schema instance.

        Returns:
            LamodaProductEntity: Lamoda domain model instance.
        """

        return LamodaProductEntity(**schema.model_dump())

    @classmethod
    def to_schema(cls, domain: LamodaProductEntity) -> LamodaProductReadSchema:
        """
        to_schema: Transform lamoda product domain model to lamoda product read schema.

        Args:
            domain (LamodaProductEntity): Lamoda product domain model instance.

        Returns:
            LamodaProductReadSchema: Lamoda product read schema instance.
        """

        return LamodaProductReadSchema.model_construct(
            sku=domain.sku,
            url=domain.url,
            category=domain.category,
            description=domain.description,
            price=domain.price,
            price_currency=domain.price_currency,
            price_valid_until=domain.price_valid_until,
            parsed_at=domain.parsed_at,
        )
