"""
game.py: File, containing publisher interface for a twich user.
"""


from abc import abstractmethod
from application.interfaces.publisher import IPublisher
from domain.events import (
    TwichUserCreated,
    TwichUserDeleted,
    TwichUserDomainEvent,
)


class ITwichUserPublisher(IPublisher[TwichUserDomainEvent]):
    @abstractmethod
    async def publish_user_created_event(self, event: TwichUserCreated) -> None:
        raise NotImplementedError

    @abstractmethod
    async def publish_user_deleted_event(self, event: TwichUserDeleted) -> None:
        raise NotImplementedError
