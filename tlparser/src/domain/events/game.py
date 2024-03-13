"""
game.py: File, containing twich game domain events.
"""


from abc import ABC
from dataclasses import dataclass
from datetime import datetime
from domain.events.base import DomainEvent


@dataclass(frozen=True)
class TwichGameDomainEvent(DomainEvent, ABC):
    """
    TwichGameDomainEvent: Class, representing twich game domain event. This class is abstract.
    All domain events related to twich game should be inherited from this class.
    You can create an instance of this class, but ABC shows that you should not do this.


    Bases:
        1) DomainEvent: Base domain event. Every domain event should be inherited from this class.
        2) ABC: Abstract Base Class. It is a marker that this class should not be instantiated.
    """

    pass


@dataclass(frozen=True)
class TwichGameCreated(TwichGameDomainEvent):
    """
    TwichGameCreated: Class, representing that twich game has been created.

    Bases:
        1) TwichGameDomainEvent: Domain event for all twich game domain events.
    """

    id: int
    name: str
    igdb_id: str
    box_art_url: str
    parsed_at: datetime


@dataclass(frozen=True)
class TwichGameDeleted(TwichGameDomainEvent):
    """
    TwichGameDeleted: Class, representing that twich game has been deleted.

    Bases:
        1) TwichGameDomainEvent: Domain event for all twich game domain events.
    """

    id: int
