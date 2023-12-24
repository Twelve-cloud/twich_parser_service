"""
stream_events.py: File, containing twich stream events.
"""


from dataclasses import dataclass
from datetime import datetime
from domain.events.base.base_event import BaseDomainEvent


@dataclass
class PublicParseStreamCalledEvent(BaseDomainEvent):
    """
    PublicParseStreamCalledEvent: Represents that public parse endpoint has been called.

    Args:
        BaseDomainEvent (_type_): Base domain event abstract class.
    """

    type: str
    user_login: str


@dataclass
class TwichStreamCreatedOrUpdatedEvent(BaseDomainEvent):
    """
    TwichStreamCreatedOrUpdatedEvent: Represents that twich stream has been created.

    Args:
        BaseDomainEvent (_type_): Base domain event abstract class.
    """

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


@dataclass
class TwichStreamDeletedByUserLoginEvent(BaseDomainEvent):
    """
    TwichStreamDeletedByUserLoginEvent: Represents that twich stream has been deleted by user login.

    Args:
        BaseDomainEvent (_type_): Base domain event abstract class.
    """

    user_login: str
