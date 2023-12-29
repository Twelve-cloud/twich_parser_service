"""
products_dispatcher.py: File, containing products kafka dispatcher.
"""


import asyncio
from pickle import loads
from threading import Thread
from kafka import KafkaConsumer
from application.interfaces.services.lamoda.products_service import ILamodaProductsService
from application.schemas.lamoda.product_schema import LamodaProductSchema
from domain.events.lamoda.products_events import (
    LamodaProductCreatedOrUpdatedEvent,
    LamodaProductsDeletedByCategoryEvent,
)


class LamodaProductsKafkaDispatcher:
    """
    LamodaProductsKafkaDispatcher: Class, that represents lamoda products kafka dispatcher.
    """

    def __init__(
        self,
        bootstrap_servers: str,
        api_version: tuple,
        topic: str,
        service: ILamodaProductsService,
    ) -> None:
        """
        __init__: Initialize lamoda products kafka dispathcer.

        Args:
            bootstrap_servers (str): Kafka host and port.
            api_version (tuple): Consumer api version.
            topic (str): Name of the topic.
            service (ILamodaProductsService): Application service.
        """

        self.consumer: KafkaConsumer = KafkaConsumer(
            bootstrap_servers=bootstrap_servers,
            api_version=api_version,
            value_deserializer=lambda v: loads(v),
        )
        self.consumer.subscribe([topic])
        self.service: ILamodaProductsService = service
        Thread(
            target=asyncio.run,
            args=(self.run(),),
            daemon=True,
        ).start()

    async def run(self) -> None:
        """
        run: Run kafka consumer for reading messages.
        """

        for event in self.consumer:
            match event.value.__class__.__name__:
                case LamodaProductCreatedOrUpdatedEvent.__name__:
                    product_schema: LamodaProductSchema = LamodaProductSchema.model_construct(
                        sku=event.value.sku,
                        url=event.value.url,
                        category=event.value.category,
                        description=event.value.description,
                        price=event.value.price,
                        price_currency=event.value.price_currency,
                        price_valid_until=event.value.price_valid_until,
                        parsed_at=event.value.parsed_at,
                    )
                    await self.service.create(product_schema)
                case LamodaProductsDeletedByCategoryEvent.__name__:
                    await self.service.delete_products_by_category(category=event.value.category)
                case _:
                    pass
