"""
game_events.py: File, containing twich game events.
"""


from dataclasses import dataclass
from datetime import datetime
from domain.events.base.base_event import BaseDomainEvent


@dataclass
class PublicParseGameCalledEvent(BaseDomainEvent):
    """
    PublicParseGameCalledEvent: Represents that public parse endpoint has been called.

    Args:
        BaseDomainEvent (_type_): Base domain event abstract class.
    """

    type: str
    name: str


@dataclass
class TwichGameCreatedOrUpdatedEvent(BaseDomainEvent):
    """
    TwichGameCreatedOrUpdatedEvent: Represents that twich game has been created.

    Args:
        BaseDomainEvent (_type_): Base domain event abstract class.
    """

    id: int
    name: str
    igdb_id: str
    box_art_url: str
    parsed_at: datetime


@dataclass
class TwichGameDeletedByNameEvent(BaseDomainEvent):
    """
    TwichGameDeletedByNameEvent: Represents that twich game has been deleted by name.

    Args:
        BaseDomainEvent (_type_): Base domain event abstract class.
    """

    name: str
