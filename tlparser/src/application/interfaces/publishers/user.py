"""
game.py: File, containing publisher interface for a twich user.
"""


from application.interfaces.publishers import IPublisher
from domain.events import (
    TwichUserCreatedEvent,
    TwichUserDeletedEvent,
    TwichUserDomainEvent,
)


class ITwichUserPublisher(IPublisher[TwichUserDomainEvent]):
    async def publish_user_created_event(self, event: TwichUserCreatedEvent) -> None:
        raise NotImplementedError

    async def publish_user_deleted_event(self, event: TwichUserDeletedEvent) -> None:
        raise NotImplementedError
