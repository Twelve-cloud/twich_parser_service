"""
game.py: File, containing publisher interface for a twich game.
"""


from application.interfaces.publishers import IPublisher
from domain.events import (
    TwichGameCreatedEvent,
    TwichGameDeletedEvent,
    TwichGameDomainEvent,
)


class ITwichGamePublisher(IPublisher[TwichGameDomainEvent]):
    async def publish_game_created_event(self, event: TwichGameCreatedEvent) -> None:
        raise NotImplementedError

    async def publish_game_deleted_event(self, event: TwichGameDeletedEvent) -> None:
        raise NotImplementedError
