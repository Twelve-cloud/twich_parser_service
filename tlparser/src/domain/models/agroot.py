"""
base.py: File, containing aggregate root.
"""


from __future__ import annotations
from abc import ABC
from dataclasses import dataclass, field
from typing import Any, Generic
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

    @staticmethod
    def dict(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        return {key: value for key, value in pairs if key != '_events'}
