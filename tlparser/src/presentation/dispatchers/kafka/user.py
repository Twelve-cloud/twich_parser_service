"""
user_dispatcher.py: File, containing user kafka dispatcher.
"""


import asyncio
from pickle import loads
from threading import Thread
from kafka import KafkaConsumer
from application.dtos.fastapi_schemas.twich.user_schema import TwichUserSchema
from application.interfaces.services.twich.user import ITwichUserService
from domain.events.user import TwichUserCreatedOrUpdatedEvent, TwichUserDeletedByLoginEvent


class TwichUserKafkaDispatcher:
    """
    TwichUserKafkaDispatcher: Class, that represents twich user kafka dispatcher.
    """

    def __init__(
        self,
        bootstrap_servers: str,
        api_version: tuple,
        topic: str,
        service: ITwichUserService,
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
        self.service: ITwichUserService = service
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
                case TwichUserCreatedOrUpdatedEvent.__name__:
                    user_schema: TwichUserSchema = TwichUserSchema.model_construct(
                        id=event.value.id,
                        login=event.value.login,
                        description=event.value.description,
                        display_name=event.value.display_name,
                        type=event.value.type,
                        broadcaster_type=event.value.broadcaster_type,
                        profile_image_url=event.value.profile_image_url,
                        offline_image_url=event.value.offline_image_url,
                        created_at=event.value.created_at,
                        parsed_at=event.value.parsed_at,
                    )
                    await self.service.create(user_schema)
                case TwichUserDeletedByLoginEvent.__name__:
                    await self.service.delete(event.value.login)
                case _:
                    pass
