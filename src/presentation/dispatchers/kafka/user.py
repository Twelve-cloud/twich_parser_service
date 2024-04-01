"""
user_dispatcher.py: File, containing user kafka dispatcher.
"""


import asyncio
from pickle import loads
from threading import Thread

from automapper import mapper
from kafka import KafkaConsumer

from application.interfaces.repository import ITwichUserRepository
from domain.events.user import (
    TwichUserCreated,
    TwichUserDeleted,
)
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
                case TwichUserCreated.__name__:
                    user: TwichUser = mapper.to(TwichUser).map(event.value)
                    await self.repository.add_or_update(user)
                case TwichUserDeleted.__name__:
                    user = await self.repository.get_by_id(event.value.id)
                    await self.repository.delete(user)
                case _:
                    pass
