"""
stream.py: File, containing twich stream domain events.
"""


from abc import ABC
from dataclasses import dataclass
from datetime import datetime
from domain.events import DomainEvent


@dataclass(frozen=True)
class TwichStreamDomainEvent(DomainEvent, ABC):
    pass


@dataclass(frozen=True)
class TwichStreamCreated(TwichStreamDomainEvent):
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
    id: int
