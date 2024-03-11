"""
__init__.py: File, containing other event modules to simplify import.
"""


from domain.events.base import DomainEvent
from domain.events.game import (
    TwichGameCreatedEvent,
    TwichGameDeletedEvent,
    TwichGameDomainEvent,
)
from domain.events.stream import (
    TwichStreamCreatedEvent,
    TwichStreamDeletedEvent,
    TwichStreamDomainEvent,
)
from domain.events.user import (
    TwichUserCreatedEvent,
    TwichUserDeletedEvent,
    TwichUserDomainEvent,
)


__all__: list[str] = [
    'DomainEvent',
    'TwichGameCreatedEvent',
    'TwichGameDeletedEvent',
    'TwichGameDomainEvent',
    'TwichStreamCreatedEvent',
    'TwichStreamDeletedEvent',
    'TwichStreamDomainEvent',
    'TwichUserCreatedEvent',
    'TwichUserDeletedEvent',
    'TwichUserDomainEvent',
]
