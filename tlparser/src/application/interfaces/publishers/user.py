"""
game.py: File, containing publisher interface for a twich user.
"""


from application.interfaces.publishers import IPublisher
from domain.events import (
    TwichUserCreated,
    TwichUserDeleted,
    TwichUserDomainEvent,
)


class ITwichUserPublisher(IPublisher[TwichUserDomainEvent]):
    async def publish_user_created_event(self, event: TwichUserCreated) -> None:
        raise NotImplementedError

    async def publish_user_deleted_event(self, event: TwichUserDeleted) -> None:
        raise NotImplementedError
