"""
base.py: File, containing base domain model and aggregate root.
"""


from abc import ABC
from dataclasses import dataclass, field
from datetime import datetime
from typing import Generic
from domain.events import DE


@dataclass(frozen=False)
class DomainModel(ABC):
    """
    DomainModel: Class, representing base domain model. This class is abstract.
    All domain models should be inherited from this class.
    You can create an instance of this class, but ABC shows that you should not do this.

    Bases:
        1) ABC: Abstract Base Class. It is a marker that this class should not be instantiated.
    """

    parsed_at: datetime


@dataclass(frozen=False)
class AggregateRoot(Generic[DE], ABC):
    """
    AggregateRoot: Class, representing aggregate root. This class is abstract.
    All domain models that are aggregate root should be inherited from this class.

    Bases:
        1) Generic[DE]: This class makes aggregate root class generic.
           Every domain model that is aggregate root might produce events.
           So, when inheriting this class, event type can be specified.
        2) ABC: Abstract Base Class. It is a marker that this class should not be instantiated.
    """

    _events: list[DE] = field(default_factory=list, init=False)

    def register_event(self, event: DE) -> None:
        """
        register_event: Registers event in local storage.

        Args:
            event (DE): Event that should be registered.
        """

        self._events.append(event)

        return

    def clear_events(self) -> None:
        """
        clear_events: Clears all events from local storage.
        """

        self._events.clear()

        return

    def get_events(self) -> list[DE]:
        """
        get_events: Returns events from local storage.

        Returns:
            list[DE]: List of events.
        """

        return self._events

    def pull_events(self) -> list[DE]:
        """
        pull_events: Clears events from local storage and returns them.

        Returns:
            list[DE]: List of events.
        """

        events: list[DE] = self.get_events().copy()
        self.clear_events()

        return events
