"""
__init__.py: File, containing other event modules to simplify import.
"""


from domain.events.base import BaseDomainEvent
from domain.events.game import (
    TwichGameCreatedEvent,
    TwichGameDeletedByNameEvent,
    TwichGameDomainEvent,
)
from domain.events.stream import (
    TwichStreamCreatedEvent,
    TwichStreamDeletedByUserLoginEvent,
    TwichStreamDomainEvent,
)
from domain.events.user import (
    TwichUserCreatedEvent,
    TwichUserDeletedByLoginEvent,
    TwichUserDomainEvent,
)


__all__: list[str] = [
    'BaseDomainEvent',
    'TwichGameCreatedEvent',
    'TwichGameDeletedByNameEvent',
    'TwichGameDomainEvent',
    'TwichStreamCreatedEvent',
    'TwichStreamDeletedByUserLoginEvent',
    'TwichStreamDomainEvent',
    'TwichUserCreatedEvent',
    'TwichUserDeletedByLoginEvent',
    'TwichUserDomainEvent',
]
