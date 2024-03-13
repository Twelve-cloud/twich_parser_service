"""
game_publisher.py: File, containing kafka publisher class for twich game.
"""


from threading import Thread
from common.config import settings
from domain.events import TwichGameCreatedEvent, TwichGameDeletedEvent, TwichGameDomainEvent
from application.interfaces.publishers import ITwichGamePublisher
from infrastructure.publishers.connections.kafka.producer import KafkaProducerConnection


class TwichGameKafkaPublisher(ITwichGamePublisher):
    def __init__(self, kafka_producer: KafkaProducerConnection) -> None:
        self.producer = kafka_producer.producer

    async def publish(self, events: list[TwichGameDomainEvent]) -> None:
        for event in events:
            if isinstance(event, TwichGameCreatedEvent):
                await self.publish_game_created_event(event)
            elif isinstance(event, TwichGameDeletedEvent):
                await self.publish_game_deleted_event(event)

        return

    async def publish_game_created_event(self, event: TwichGameCreatedEvent) -> None:
        Thread(
            target=self.producer.send,
            args=(settings.KAFKA_GAME_TOPIC, event),
            daemon=True,
        ).start()

    async def publish_game_deleted_event(self, event: TwichGameDeletedEvent) -> None:
        Thread(
            target=self.producer.send,
            args=(settings.KAFKA_GAME_TOPIC, event),
            daemon=True,
        ).start()
