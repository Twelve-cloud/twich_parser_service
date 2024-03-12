"""
user.py: File, containing twich user domain events.
"""


from abc import ABC
from dataclasses import dataclass
from datetime import datetime
from domain.events import DomainEvent


@dataclass(frozen=True)
class TwichUserDomainEvent(DomainEvent, ABC):
    pass


@dataclass(frozen=True)
class TwichUserCreated(TwichUserDomainEvent):
    id: int
    login: str
    description: str
    display_name: str
    type: str
    broadcaster_type: str
    profile_image_url: str
    offline_image_url: str
    created_at: datetime
    parsed_at: datetime


@dataclass(frozen=True)
class TwichUserDeleted(TwichUserDomainEvent):
    id: int
