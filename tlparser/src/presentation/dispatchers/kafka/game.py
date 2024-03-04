"""
game_dispatcher.py: File, containing game kafka dispatcher.
"""


import asyncio
from pickle import loads
from threading import Thread
from kafka import KafkaConsumer
from application.dtos.fastapi_schemas.twich.game_schema import TwichGameSchema
from application.interfaces.services.twich.game import ITwichGameService
from domain.events.game import TwichGameCreatedOrUpdatedEvent, TwichGameDeletedByNameEvent


class TwichGameKafkaDispatcher:
    """
    TwichGameKafkaDispatcher: Class, that represents twich game kafka dispatcher.
    """

    def __init__(
        self,
        bootstrap_servers: str,
        api_version: tuple,
        topic: str,
        service: ITwichGameService,
    ) -> None:
        """
        __init__: Initialize twich game kafka dispathcer.

        Args:
            bootstrap_servers (str): Kafka host and port.
            api_version (tuple): Consumer api version.
            topic (str): Name of the topic.
            service (ITwichGameService): Application service.
        """

        self.consumer: KafkaConsumer = KafkaConsumer(
            bootstrap_servers=bootstrap_servers,
            api_version=api_version,
            value_deserializer=lambda v: loads(v),
        )
        self.consumer.subscribe([topic])
        self.service: ITwichGameService = service
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
                case TwichGameCreatedOrUpdatedEvent.__name__:
                    game_schema: TwichGameSchema = TwichGameSchema.model_construct(
                        id=event.value.id,
                        name=event.value.name,
                        igdb_id=event.value.igdb_id,
                        box_art_url=event.value.box_art_url,
                        parsed_at=event.value.parsed_at,
                    )
                    await self.service.create(game_schema)
                case TwichGameDeletedByNameEvent.__name__:
                    await self.service.delete(event.value.name)
                case _:
                    pass
