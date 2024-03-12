"""
stream.py: File, containing publisher interface for a twich stream.
"""


from application.interfaces.publishers import IPublisher
from domain.events import (
    TwichStreamCreated,
    TwichStreamDeleted,
    TwichStreamDomainEvent,
)


class ITwichStreamPublisher(IPublisher[TwichStreamDomainEvent]):
    async def publish_stream_created_event(self, event: TwichStreamCreated) -> None:
        raise NotImplementedError

    async def publish_stream_deleted_event(self, event: TwichStreamDeleted) -> None:
        raise NotImplementedError
