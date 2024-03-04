"""
base.py: File, containing base domain model.
"""


from datetime import datetime
from typing import Generic, TypeVar
from domain.events import BaseDomainEvent


E = TypeVar('E', bound=BaseDomainEvent)


class BaseDomainModel(Generic[E]):
    """
    BaseModel: Class, that represents base domain model for all domain models.
    It contains common data and behaviour for every domain model.

    Args:
        Generic: Base class for base domain model that make this class template.
    """

    def __init__(self, parsed_at: datetime) -> None:
        """
        __init__: Initialize base domain model instance.

        Args:
            parsed_at (datetime): Parsing date of the domain model instance.
        """

        self.parsed_at: datetime = parsed_at
        self.events: list[E] = []

    def register_event(self, event: E) -> None:
        """
        register_event: Register domain events in self.events attribute.

        Args:
            event (E): Event that should be registered.
        """

        self.events.append(event)
