"""
game.py: File, containing twich game domain events.
"""


from dataclasses import dataclass
from datetime import datetime
from domain.events import BaseDomainEvent


@dataclass
class TwichGameDomainEvent(BaseDomainEvent):
    """
    TwichGameDomainEvent: Class that represents base domain event class for twich games.

    Args:
        BaseDomainEvent: Base domain event class.
    """

    pass


@dataclass
class TwichGameCreatedEvent(TwichGameDomainEvent):
    """
    TwichGameCreatedEvent: Class that represents domain event.
    That domain event represents that twich game has been created.

    Args:
        TwichGameDomainEvent: Base domain event class for twich games.
    """

    id: int
    name: str
    igdb_id: str
    box_art_url: str
    parsed_at: datetime


@dataclass
class TwichGameDeletedEvent(TwichGameDomainEvent):
    """
    TwichGameDeletedEvent: Class that represents domain event.
    That domain event represents that twich game has been deleted.

    Args:
        TwichGameDomainEvent: Base domain event class for twich games.
    """

    id: int
    name: str
    igdb_id: str
    box_art_url: str
    parsed_at: datetime
