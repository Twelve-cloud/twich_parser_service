"""
game_dispatcher.py: File, containing game kafka dispatcher.
"""


from pickle import loads
from threading import Thread
from kafka import KafkaConsumer
from domain.entities.twich.game_entity import TwichGameEntity
from domain.events.twich.game_events import (
    TwichGameCreatedOrUpdatedEvent,
    TwichGameDeletedByNameEvent,
)
from domain.repositories.twich.game_repository import TwichGameRepository


class TwichGameKafkaDispatcher:
    """
    TwichGameKafkaDispatcher: Class, that represents twich game kafka dispatcher.
    """

    def __init__(
        self,
        bootstrap_servers: str,
        api_version: tuple,
        topic: str,
        repository: TwichGameRepository,
    ) -> None:
        """
        __init__: Initialize twich game kafka dispathcer.

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
        self.repository: TwichGameRepository = repository
        Thread(target=self.run, args=()).start()

    def run(self) -> None:
        """
        run: Run kafka consumer for reading messages.
        """

        for event in self.consumer:
            match event.value.__class__.__name__:
                case TwichGameCreatedOrUpdatedEvent.__name__:
                    game_entity: TwichGameEntity = TwichGameEntity(
                        id=event.value.id,
                        name=event.value.name,
                        igdb_id=event.value.igdb_id,
                        box_art_url=event.value.box_art_url,
                        parsed_at=event.value.parsed_at,
                    )
                    self.repository.create_or_update(game_entity)
                case TwichGameDeletedByNameEvent.__name__:
                    self.repository.delete_game_by_name(name=event.value.name)
                case _:
                    pass
