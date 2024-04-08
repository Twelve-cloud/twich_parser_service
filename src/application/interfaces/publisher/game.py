"""
game.py: File, containing publisher interface for a twich game.
"""


from abc import abstractmethod

from application.interfaces.publisher import IPublisher
from domain.events import (
    TwichGameCreated,
    TwichGameDeleted,
    TwichGameDomainEvent,
)


class ITwichGamePublisher(IPublisher[TwichGameDomainEvent]):
    @abstractmethod
    async def publish_game_created_event(self, event: TwichGameCreated) -> None:
        raise NotImplementedError

    @abstractmethod
    async def publish_game_deleted_event(self, event: TwichGameDeleted) -> None:
        raise NotImplementedError
