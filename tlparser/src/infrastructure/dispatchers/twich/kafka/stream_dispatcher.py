"""
stream_dispatcher.py: File, containing stream kafka dispatcher.
"""


from pickle import loads
from threading import Thread
from kafka import KafkaConsumer
from domain.entities.twich.stream_entity import TwichStreamEntity
from domain.events.twich.stream_events import (
    TwichStreamCreatedOrUpdatedEvent,
    TwichStreamDeletedByUserLoginEvent,
)
from domain.repositories.twich.stream_repository import ITwichStreamRepository


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
        """

        self.consumer: KafkaConsumer = KafkaConsumer(
            bootstrap_servers=bootstrap_servers,
            api_version=api_version,
            value_deserializer=lambda v: loads(v),
        )
        self.consumer.subscribe([topic])
        self.repository: ITwichStreamRepository = repository
        Thread(target=self.run, args=()).start()

    def run(self) -> None:
        """
        run: Run kafka consumer for reading messages.
        """

        for event in self.consumer:
            match event.value.__class__.__name__:
                case TwichStreamCreatedOrUpdatedEvent.__name__:
                    stream_entity: TwichStreamEntity = TwichStreamEntity(
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
                    self.repository.create_or_update(stream_entity)
                case TwichStreamDeletedByUserLoginEvent.__name__:
                    self.repository.delete_stream_by_user_login(user_login=event.value.user_login)
                case _:
                    pass
