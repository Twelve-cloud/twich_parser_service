"""
user_events.py: File, containing twich user events.
"""


from dataclasses import dataclass
from datetime import datetime
from domain.events.base.base_event import BaseDomainEvent


@dataclass
class PublicParseUserCalledEvent(BaseDomainEvent):
    """
    PublicParseUserCalledEvent: Represents that public parse endpoint has been called.

    Args:
        BaseDomainEvent (_type_): Base domain event abstract class.
    """

    type: str
    login: str


@dataclass
class TwichUserCreatedOrUpdatedEvent(BaseDomainEvent):
    """
    TwichUserCreatedOrUpdatedEvent: Represents that twich user has been created.

    Args:
        BaseDomainEvent (_type_): Base domain event abstract class.
    """

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


@dataclass
class TwichUserDeletedByLoginEvent(BaseDomainEvent):
    """
    TwichUserDeletedByLoginEvent: Represents that twich user has been deleted by login.

    Args:
        BaseDomainEvent (_type_): Base domain event abstract class.
    """

    login: str
