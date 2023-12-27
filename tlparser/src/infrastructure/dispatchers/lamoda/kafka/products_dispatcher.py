"""
products_dispatcher.py: File, containing products kafka dispatcher.
"""


from pickle import loads
from threading import Thread
from kafka import KafkaConsumer
from domain.entities.lamoda.product_entity import LamodaProductEntity
from domain.events.lamoda.products_events import (
    LamodaProductCreatedOrUpdatedEvent,
    LamodaProductsDeletedByCategoryEvent,
)
from domain.repositories.lamoda.products_repository import LamodaProductsRepository


class LamodaProductsKafkaDispatcher:
    """
    LamodaProductsKafkaDispatcher: Class, that represents lamoda products kafka dispatcher.
    """

    def __init__(
        self,
        bootstrap_servers: str,
        api_version: tuple,
        topic: str,
        repository: LamodaProductsRepository,
    ) -> None:
        """
        __init__: Initialize lamoda products kafka dispathcer.

        Args:
            bootstrap_servers (str): Kafka host and port.
            api_version (tuple): Consumer api version.
            topic (str): Name of the topic.
        """

        self.consumer: KafkaConsumer = KafkaConsumer(
            bootstrap_servers=bootstrap_servers,
            api_version=api_version,
            value_deserializer=lambda v: loads(v),
        )
        self.consumer.subscribe([topic])
        self.repository: LamodaProductsRepository = repository
        Thread(target=self.run, args=()).start()

    def run(self) -> None:
        """
        run: Run kafka consumer for reading messages.
        """

        for event in self.consumer:
            match event.value.__class__.__name__:
                case LamodaProductCreatedOrUpdatedEvent.__name__:
                    products_entity: LamodaProductEntity = LamodaProductEntity(
                        sku=event.value.sku,
                        url=event.value.url,
                        category=event.value.category,
                        description=event.value.description,
                        price=event.value.price,
                        price_currency=event.value.price_currency,
                        price_valid_until=event.value.price_valid_until,
                        parsed_at=event.value.parsed_at,
                    )
                    self.repository.create_or_update(products_entity)
                case LamodaProductsDeletedByCategoryEvent.__name__:
                    self.repository.delete_products_by_category(category=event.value.category)
                case _:
                    pass
