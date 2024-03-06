"""
stream.py: File, containing twich stream domain events.
"""


from dataclasses import dataclass
from datetime import datetime
from domain.events import BaseDomainEvent


@dataclass
class TwichStreamDomainEvent(BaseDomainEvent):
    """
    TwichStreamDomainEvent: Class that represents base domain event class for twich streams.

    Args:
        BaseDomainEvent: Base domain event class.
    """

    pass


@dataclass
class TwichStreamCreatedEvent(TwichStreamDomainEvent):
    """
    TwichStreamCreatedEvent: Class that represents domain event.
    That domain event represents that twich stream has been created.

    Args:
        TwichStreamDomainEvent: Base domain event class for twich streams.
    """

    id: int
    user_id: int
    user_name: str
    user_login: str
    game_id: int
    game_name: str
    language: str
    title: str
    tags: list[str]
    started_at: datetime
    viewer_count: int
    type: str
    parsed_at: datetime


@dataclass
class TwichStreamDeletedEvent(TwichStreamDomainEvent):
    """
    TwichStreamDeletedEvent: Class that represents domain event.
    That domain event represents that twich stream has been deleted.

    Args:
        TwichStreamDomainEvent: Base domain event class for twich streams.
    """

    id: int
    user_id: int
    user_name: str
    user_login: str
    game_id: int
    game_name: str
    language: str
    title: str
    tags: list[str]
    started_at: datetime
    viewer_count: int
    type: str
    parsed_at: datetime
