"""
stream_dispatcher.py: File, containing stream kafka dispatcher.
"""


import asyncio
from pickle import loads
from threading import Thread
from automapper import mapper
from kafka import KafkaConsumer
from domain.events.stream import TwichStreamCreatedEvent, TwichStreamDeletedByUserLoginEvent
from domain.interfaces.repositories import ITwichStreamRepository
from domain.models import TwichStream


class TwichStreamKafkaDispatcher:
    """
    TwichStreamKafkaDispatcher: Class, that represents twich stream kafka dispatcher.
    """

    def __init__(
        self,
        bootstrap_servers: str,
        api_version: tuple,
        topic: str,
        repository: ITwichStreamRepository,
    ) -> None:
        """
        __init__: Initialize twich stream kafka dispatcher.

        Args:
            bootstrap_servers (str): Kafka host and port.
            api_version (tuple): Consumer api version.
            topic (str): Name of the topic.
            service (ITwichStreamService): Application service.
        """

        self.consumer: KafkaConsumer = KafkaConsumer(
            bootstrap_servers=bootstrap_servers,
            api_version=api_version,
            value_deserializer=lambda v: loads(v),
        )
        self.consumer.subscribe([topic])
        self.repository: ITwichStreamRepository = repository
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
                case TwichStreamCreatedEvent.__name__:
                    stream: TwichStream = mapper.to(TwichStream).map(event)
                    await self.repository.add_or_update(stream)
                case TwichStreamDeletedByUserLoginEvent.__name__:
                    stream = mapper.to(TwichStream).map(event)
                    await self.repository.delete(stream)
                case _:
                    pass
