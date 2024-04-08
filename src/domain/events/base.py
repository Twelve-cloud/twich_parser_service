"""
base.py: File, containing base domain event.
"""


from abc import ABC
from dataclasses import (
    dataclass,
    field,
)
from datetime import datetime
from uuid import (
    UUID,
    uuid4,
)


@dataclass(frozen=True)
class DomainEvent(ABC):
    event_id: UUID = field(default_factory=uuid4, init=False)
    event_timestamp: datetime = field(default_factory=datetime.utcnow, init=False)
