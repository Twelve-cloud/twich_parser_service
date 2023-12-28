"""
products_service.py: File, containing service for lamoda products.
"""


from application.mappers.lamoda.product_mapper import LamodaProductMapper
from application.schemas.lamoda.product_schema import LamodaProductSchema
from domain.entities.lamoda.product_entity import LamodaProductEntity
from domain.events.lamoda.products_events import (
    LamodaProductCreatedOrUpdatedEvent,
    LamodaProductsDeletedByCategoryEvent,
    PublicParseProductsCalledEvent,
)
from domain.interfaces.publishers.lamoda.products_publisher import ILamodaProductsPublisher
from domain.interfaces.repositories.lamoda.products_repository import ILamodaProductsRepository
from domain.services.lamoda.products_service import LamodaProductsDomainService
from domain.types.types import ResultWithEvent


class LamodaProductsRestService:
    """
    LamodaProductsRestService: Class, that contains business logic for lamoda products.
    """

    def __init__(
        self,
        domain_service: LamodaProductsDomainService,
        publisher: ILamodaProductsPublisher,
        repository: ILamodaProductsRepository,
    ) -> None:
        """
        __init__: Do some initialization for LamodaProductsRestService class.

        Args:
            domain_service (LamodaProductsDomainService): Lamoda products domain service.
            publisher (ILamodaProductsPublisher): Lamoda products publisher.
            repository (ILamodaProductsRepository): Lamoda products repository.
        """

        self.domain_service: LamodaProductsDomainService = domain_service
        self.publisher: ILamodaProductsPublisher = publisher
        self.repository: ILamodaProductsRepository = repository

    async def parse_products(self, category: str) -> None:
        """
        parse_products: Called lamoda products publisher to publish event about parsing.

        Args:
            category (str): Category lamoda url.
        """

        event: PublicParseProductsCalledEvent = await self.repository.parse_products(category)

        await self.publisher.publish_parse_products_called_event(event)

        return

    async def private_parse_products(self, category: str) -> list[LamodaProductSchema]:
        """
        private_parse_products: Parse lamoda products by category.

        Args:
            category (str): Category lamoda url.

        Returns:
            list[LamodaProductSchema]: List of LamodaProductEntity instances.
        """

        product_schemas: list[LamodaProductSchema] = []

        product_entities: list[LamodaProductEntity] = await self.domain_service.parse_products(
            category,
        )

        for product_entity in product_entities:
            product_entity_with_event: ResultWithEvent[
                LamodaProductEntity, LamodaProductCreatedOrUpdatedEvent
            ] = await self.repository.create_or_update(product_entity)

            await self.publisher.publish_created_or_updated_event(product_entity_with_event.event)

            product_schemas.append(LamodaProductMapper.to_schema(product_entity_with_event.result))

        return product_schemas

    async def create(self, schema: LamodaProductSchema) -> None:
        """
        create: Create lamoda product.

        Args:
            schema (LamodaProductSchema): Lamoda product schema.
        """

        await self.repository.create_or_update(LamodaProductMapper.to_domain(schema))

        return

    async def delete_products_by_category(self, category: str) -> None:
        """
        delete_products_by_category: Delete products by category.

        Args:
            category (str): Category lamoda url.
        """

        event: LamodaProductsDeletedByCategoryEvent = (
            await self.repository.delete_products_by_category(category)
        )

        await self.publisher.publish_products_deleted_by_category_event(event)

        return

    async def get_all_products(self) -> list[LamodaProductSchema]:
        """
        get_all_products: Return all products.

        Returns:
            list[LamodaProductSchema]: List of lamoda products.
        """

        return [
            LamodaProductMapper.to_schema(product_entity)
            for product_entity in await self.repository.all()
        ]

    async def get_products_by_category(self, category: str) -> list[LamodaProductSchema]:
        """
        get_products_by_category: Return products by category.

        Args:
            category (str): Category lamoda url.

        Returns:
            list[LamodaProductSchema]: List of lamoda products with the same category.
        """

        return [
            LamodaProductMapper.to_schema(product_entity)
            for product_entity in await self.repository.get_products_by_category(category)
        ]
