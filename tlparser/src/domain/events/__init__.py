"""
__init__.py: File, containing other event modules to simplify import.
"""


from domain.events.base import DomainEvent
from domain.events.game import (
    TwichGameCreated,
    TwichGameDeleted,
    TwichGameDomainEvent,
)
from domain.events.stream import (
    TwichStreamCreated,
    TwichStreamDeleted,
    TwichStreamDomainEvent,
)
from domain.events.user import (
    TwichUserCreated,
    TwichUserDeleted,
    TwichUserDomainEvent,
)


__all__: list[str] = [
    'DomainEvent',
    'TwichGameCreated',
    'TwichGameDeleted',
    'TwichGameDomainEvent',
    'TwichStreamCreated',
    'TwichStreamDeleted',
    'TwichStreamDomainEvent',
    'TwichUserCreated',
    'TwichUserDeleted',
    'TwichUserDomainEvent',
]
