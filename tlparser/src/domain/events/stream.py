"""
stream.py: File, containing twich stream domain events.
"""


from abc import ABC
from dataclasses import dataclass
from datetime import datetime
from domain.events.base import DomainEvent


@dataclass(frozen=True)
class TwichStreamDomainEvent(DomainEvent, ABC):
    """
    TwichStreamDomainEvent: Class, representing twich stream domain event. This class is abstract.
    All domain events related to twich stream should be inherited from this class.
    You can create an instance of this class, but ABC shows that you should not do this.


    Bases:
        1) DomainEvent: Base domain event. Every domain event should be inherited from this class.
        2) ABC: Abstract Base Class. It is a marker that this class should not be instantiated.
    """

    pass


@dataclass(frozen=True)
class TwichStreamCreated(TwichStreamDomainEvent):
    """
    TwichStreamCreated: Class, representing that twich stream has been created.

    Bases:
        1) TwichStreamDomainEvent: Domain event for all twich stream domain events.
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


@dataclass(frozen=True)
class TwichStreamDeleted(TwichStreamDomainEvent):
    """
    TwichStreamDeleted: Class, representing that twich stream has been deleted.

    Bases:
        1) TwichStreamDomainEvent: Domain event for all twich stream domain events.
    """

    id: int
