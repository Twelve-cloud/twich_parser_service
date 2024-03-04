"""
user.py: File, containing twich user domain events.
"""


from dataclasses import dataclass
from datetime import datetime
from domain.events import BaseDomainEvent


@dataclass
class TwichUserDomainEvent(BaseDomainEvent):
    """
    TwichUserDomainEvent: Class that represents base domain event class for twich users.

    Args:
        BaseDomainEvent: Base domain event class.
    """

    pass


@dataclass
class TwichUserCreatedEvent(TwichUserDomainEvent):
    """
    TwichUserCreatedEvent: Class that represents domain event.
    That domain event represents that twich user has been created.

    Args:
        TwichUserDomainEvent: Base domain event class for twich users.
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
class TwichUserDeletedByLoginEvent(TwichUserDomainEvent):
    """
    TwichUserDeletedByLoginEvent: Class that represents domain event.
    That domain event represents that twich user has been deleted.

    Args:
        TwichUserDomainEvent: Base domain event class for twich users.
    """

    login: str
