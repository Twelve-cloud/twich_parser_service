"""
root.py: File, containing aggregate root.
"""


from abc import ABC
from dataclasses import dataclass, field
from typing import Generic, TypeVar
from domain.events import DomainEvent


E = TypeVar('E', bound=DomainEvent)


@dataclass(frozen=False)
class AggregateRoot(Generic[E], ABC):
    _events: list[E] = field(default_factory=list, init=False)

    def register_event(self, event: E) -> None:
        self._events.append(event)

        return

    def clear_events(self) -> None:
        self._events.clear()

        return

    def get_events(self) -> list[E]:
        return self._events

    def pull_events(self) -> list[E]:
        events: list[E] = self.get_events().copy()
        self.clear_events()

        return events
