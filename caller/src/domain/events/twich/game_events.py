"""
game_events.py: File, containing twich game events.
"""


from dataclasses import dataclass
from domain.events.base.base_event import BaseDomainEvent


@dataclass
class PublicParseGameCalledEvent(BaseDomainEvent):
    """
    PublicParseGameCalledEvent: Represents that public parse endpoint has been called.

    Args:
        BaseDomainEvent (_type_): Base domain event abstract class.
    """

    name: str
