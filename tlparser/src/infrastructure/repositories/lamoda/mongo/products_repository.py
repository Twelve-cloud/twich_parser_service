"""
products_repository.py: File, containing lamoda products mongo repository implementation.
"""


from domain.entities.lamoda.product_entity import LamodaProductEntity
from domain.events.lamoda.products_events import (
    LamodaProductCreatedOrUpdatedEvent,
    LamodaProductsDeletedByCategoryEvent,
    PublicParseProductsCalledEvent,
)
from domain.repositories.base.base_repository import ResultWithEvent
from domain.repositories.lamoda.products_repository import LamodaProductsRepository
from infrastructure.connections.mongo.database import MongoDatabase
from infrastructure.mappers.lamoda.mongo.product_mapper import LamodaProductMapper
from infrastructure.models.lamoda.mongo.product_model import LamodaProduct


class LamodaProductsMongoRepository(LamodaProductsRepository):
    """
    LamodaProductsMongoRepository: Mongo implementation of LamodaProductsRepository.

    Args:
        LamodaProductsRepository (_type_): Repository abstract class.
    """

    def __init__(self, db: MongoDatabase) -> None:
        """
        __init__: Initialize repository.

        Args:
            db (MongoDatabase): MongoDatabase instance, containing mongo connection.
        """

        self.db: MongoDatabase = db

    def parse_products(self, category: str) -> PublicParseProductsCalledEvent:
        """
        parse_products: Return event about parsing products.

        Args:
            category (str): Products category.

        Returns:
            PublicParseProductsCalledEvent: Event about parsing products.
        """

        return PublicParseProductsCalledEvent(type='lamoda_product', category=category)

    def create_or_update(
        self, product_entity: LamodaProductEntity
    ) -> ResultWithEvent[LamodaProductEntity, LamodaProductCreatedOrUpdatedEvent]:
        """
        create_or_update: Create or update lamoda product.

        Args:
            product_entity (LamodaProductEntity): Lamoda product entity.

        Returns:
            ResultWithEvent[Result, Event]: Created/updated lamoda product entity with event.
        """

        product_persistence = LamodaProductMapper.to_persistence(product_entity)
        product_persistence.save()

        event: LamodaProductCreatedOrUpdatedEvent = LamodaProductCreatedOrUpdatedEvent(
            sku=product_persistence.sku,
            url=product_persistence.url,
            category=product_persistence.category,
            description=product_persistence.description,
            price=product_persistence.price,
            price_currency=product_persistence.price_currency,
            price_valid_until=product_persistence.price_valid_until,
            parsed_at=product_persistence.parsed_at,
        )
        entity: LamodaProductEntity = LamodaProductMapper.to_domain(product_persistence)

        return ResultWithEvent[LamodaProductEntity, LamodaProductCreatedOrUpdatedEvent](
            result=entity,
            event=event,
        )

    def all(self) -> list[LamodaProductEntity]:
        """
        all: Return list of lamoda products.

        Returns:
            list[LamodaProductEntity]: List of lamoda products.
        """

        return [
            LamodaProductMapper.to_domain(product_persistence)
            for product_persistence in LamodaProduct.objects
        ]

    def delete_products_by_category(self, category: str) -> LamodaProductsDeletedByCategoryEvent:
        """
        delete_products_by_category: Delete lamoda products by category.

        Args:
            category (str): Category of the products.

        Returns:
            LamodaProductsDeletedByCategoryEvent: Lamoda products deleted event.
        """

        for product_persistence in LamodaProduct.objects(category=category):
            product_persistence.delete()

        return LamodaProductsDeletedByCategoryEvent(category=category)

    def get_products_by_category(self, category: str) -> list[LamodaProductEntity]:
        """
        get_products_by_category: Return lamoda products with the same category.

        Args:
            category (str): Category of the products.

        Returns:
            list[LamodaProductEntity]: Lamoda product instance.
        """

        return [
            LamodaProductMapper.to_domain(product_persistence)
            for product_persistence in LamodaProduct.objects(category=category)
        ]
