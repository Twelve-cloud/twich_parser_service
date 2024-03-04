"""
stream_dispatcher.py: File, containing stream kafka dispatcher.
"""


import asyncio
from pickle import loads
from threading import Thread
from kafka import KafkaConsumer
from application.dtos.fastapi_schemas.twich.stream_schema import TwichStreamSchema
from application.interfaces.services.twich.stream import ITwichStreamService
from domain.events.stream import (
    TwichStreamCreatedOrUpdatedEvent,
    TwichStreamDeletedByUserLoginEvent,
)


class TwichStreamKafkaDispatcher:
    """
    TwichStreamKafkaDispatcher: Class, that represents twich stream kafka dispatcher.
    """

    def __init__(
        self,
        bootstrap_servers: str,
        api_version: tuple,
        topic: str,
        service: ITwichStreamService,
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
        self.service: ITwichStreamService = service
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
                case TwichStreamCreatedOrUpdatedEvent.__name__:
                    stream_schema: TwichStreamSchema = TwichStreamSchema.model_construct(
                        id=event.value.id,
                        user_id=event.value.user_id,
                        user_name=event.value.user_name,
                        user_login=event.value.user_login,
                        game_id=event.value.game_id,
                        game_name=event.value.game_name,
                        language=event.value.language,
                        title=event.value.title,
                        tags=event.value.tags,
                        started_at=event.value.started_at,
                        viewer_count=event.value.viewer_count,
                        type=event.value.type,
                        parsed_at=event.value.parsed_at,
                    )
                    await self.service.create(stream_schema)
                case TwichStreamDeletedByUserLoginEvent.__name__:
                    await self.service.delete(event.value.user_login)
                case _:
                    pass
