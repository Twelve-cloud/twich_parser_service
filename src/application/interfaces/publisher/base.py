"""
base.py: File, containing base publisher interface.
"""


from abc import (
    ABC as Interface,
    abstractmethod,
)
from typing import (
    Generic,
    TypeVar,
)

from domain.events import DomainEvent


E = TypeVar('E', bound=DomainEvent)


class IPublisher(Interface, Generic[E]):
    @abstractmethod
    async def publish(self, events: list[E]) -> None:
        raise NotImplementedError
