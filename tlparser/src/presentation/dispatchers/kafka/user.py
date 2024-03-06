"""
user_dispatcher.py: File, containing user kafka dispatcher.
"""


import asyncio
from pickle import loads
from threading import Thread
from automapper import mapper
from kafka import KafkaConsumer
from domain.events.user import TwichUserCreatedEvent, TwichUserDeletedByLoginEvent
from domain.interfaces.repositories import ITwichUserRepository
from domain.models import TwichUser


class TwichUserKafkaDispatcher:
    """
    TwichUserKafkaDispatcher: Class, that represents twich user kafka dispatcher.
    """

    def __init__(
        self,
        bootstrap_servers: str,
        api_version: tuple,
        topic: str,
        repository: ITwichUserRepository,
    ) -> None:
        """
        __init__: Initialize twich user kafka dispathcer.

        Args:
            bootstrap_servers (str): Kafka host and port.
            api_version (tuple): Consumer api version.
            topic (str): Name of the topic.
            service (ITwichUserService): Application service.
        """

        self.consumer: KafkaConsumer = KafkaConsumer(
            bootstrap_servers=bootstrap_servers,
            api_version=api_version,
            value_deserializer=lambda v: loads(v),
        )
        self.consumer.subscribe([topic])
        self.repository: ITwichUserRepository = repository
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
                case TwichUserCreatedEvent.__name__:
                    user: TwichUser = mapper.to(TwichUser).map(event)
                    await self.repository.add_or_update(user)
                case TwichUserDeletedByLoginEvent.__name__:
                    user = mapper.to(TwichUser).map(event)
                    await self.repository.delete(user)
                case _:
                    pass
