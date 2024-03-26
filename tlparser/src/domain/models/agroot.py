"""
base.py: File, containing aggregate root.
"""


from abc import ABC
from dataclasses import dataclass, field
from typing import Generic
from domain.events import DE


@dataclass(frozen=False)
class AggregateRoot(Generic[DE], ABC):
    _events: list[DE] = field(default_factory=list, init=False)

    def register_event(self, event: DE) -> None:
        self._events.append(event)

        return

    def clear_events(self) -> None:
        self._events.clear()

        return

    def pull_events(self) -> list[DE]:
        events: list[DE] = self.get_events().copy()
        self.clear_events()

        return events

    def get_events(self) -> list[DE]:
        return self._events
