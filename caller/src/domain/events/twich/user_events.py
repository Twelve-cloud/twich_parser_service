"""
user_events.py: File, containing twich user events.
"""


from dataclasses import dataclass
from domain.events.base.base_event import BaseDomainEvent


@dataclass
class PublicParseUserCalledEvent(BaseDomainEvent):
    """
    PublicParseUserCalledEvent: Represents that public parse endpoint has been called.

    Args:
        BaseDomainEvent (_type_): Base domain event abstract class.
    """

    login: str
