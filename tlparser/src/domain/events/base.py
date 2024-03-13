"""
base.py: File, containing base domain event.
"""


from abc import ABC
from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


@dataclass(frozen=True)
class DomainEvent(ABC):
    """
    DomainEvent: Class, representing base domain event. This class is abstract.
    All domain events should be inherited from this class.
    You can create an instance of this class, but ABC shows that you should not do this.

    Args:
        ABC: Abstract Base Class. It is a marker that this class should not be instantiated.
    """

    event_id: UUID = field(default_factory=uuid4, init=False)
    event_timestamp: datetime = field(default_factory=datetime.utcnow, init=False)
