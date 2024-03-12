"""
base.py: File, containing base publisher interface.
"""


from typing import Generic, TypeVar
from interface import Interface
from domain.events import DomainEvent


E = TypeVar('E', bound=DomainEvent)


class IPublisher(Generic[E], Interface):
    async def publish(self, events: list[E]) -> None:
        raise NotImplementedError
