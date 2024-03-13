"""
game.py: File, containing twich game domain events.
"""


from abc import ABC
from dataclasses import dataclass
from datetime import datetime
from domain.events import DomainEvent


@dataclass(frozen=True)
class TwichGameDomainEvent(DomainEvent, ABC):
    """
    TwichGameDomainEvent: Class, representing twich game domain event. This class is abstract.
    All domain events related to twich game should be inherited from this class.
    You can create an instance of this class, but ABC shows that you should not do this.


    Args:
        DomainEvent: Base domain event. Every domain event should be inherited from this class.
        ABC: Abstract Base Class. It is a marker that this class should not be instantiated.
    """

    pass


@dataclass(frozen=True)
class TwichGameCreated(TwichGameDomainEvent):
    """
    TwichGameCreated: Class, representing that twich game has been created.

    Args:
        TwichGameDomainEvent: Domain event for all twich game domain events.
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

    Args:
        TwichGameDomainEvent: Domain event for all twich game domain events.
    """

    id: int
