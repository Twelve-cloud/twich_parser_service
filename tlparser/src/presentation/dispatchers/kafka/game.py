"""
game_dispatcher.py: File, containing game kafka dispatcher.
"""


import asyncio
from pickle import loads
from threading import Thread
from automapper import mapper
from kafka import KafkaConsumer
from domain.events import TwichGameCreated, TwichGameDeleted
from application.interfaces.repository import ITwichGameRepository
from domain.models import TwichGame


class TwichGameKafkaDispatcher:
    """
    TwichGameKafkaDispatcher: Class, that represents twich game kafka dispatcher.
    """

    def __init__(
        self,
        bootstrap_servers: str,
        api_version: tuple,
        topic: str,
        repository: ITwichGameRepository,
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
        self.repository: ITwichGameRepository = repository
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
                case TwichGameCreated.__name__:
                    game: TwichGame = mapper.to(TwichGame).map(event.value)
                    await self.repository.add_or_update(game)
                case TwichGameDeleted.__name__:
                    game = await self.repository.get_by_id(event.value.id)
                    await self.repository.delete(game)
                case _:
                    pass
