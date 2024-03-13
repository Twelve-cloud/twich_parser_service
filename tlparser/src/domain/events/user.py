"""
user.py: File, containing twich user domain events.
"""


from abc import ABC
from dataclasses import dataclass
from datetime import datetime
from domain.events import DomainEvent


@dataclass(frozen=True)
class TwichUserDomainEvent(DomainEvent, ABC):
    """
    TwichUserDomainEvent: Class, representing twich user domain event. This class is abstract.
    All domain events related to twich user should be inherited from this class.
    You can create an instance of this class, but ABC shows that you should not do this.


    Args:
        DomainEvent: Base domain event. Every domain event should be inherited from this class.
        ABC: Abstract Base Class. It is a marker that this class should not be instantiated.
    """

    pass


@dataclass(frozen=True)
class TwichUserCreated(TwichUserDomainEvent):
    """
    TwichUserCreated: Class, representing that twich user has been created.

    Args:
        TwichUserDomainEvent: Domain event for all twich user domain events.
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


@dataclass(frozen=True)
class TwichUserDeleted(TwichUserDomainEvent):
    """
    TwichUserDeleted: Class, representing that twich user has been deleted.

    Args:
        TwichUserDomainEvent: Domain event for all twich user domain events.
    """

    id: int
