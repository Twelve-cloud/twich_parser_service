"""
game.py: File, containing twich game domain events.
"""


from abc import ABC
from dataclasses import dataclass
from datetime import datetime

from domain.events.base import DomainEvent


@dataclass(frozen=True)
class TwichGameDomainEvent(DomainEvent, ABC):
    pass


@dataclass(frozen=True)
class TwichGameCreated(TwichGameDomainEvent):
    id: int
    name: str
    igdb_id: str
    box_art_url: str
    parsed_at: datetime


@dataclass(frozen=True)
class TwichGameDeleted(TwichGameDomainEvent):
    id: int
