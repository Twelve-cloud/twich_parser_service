"""
base.py: File, containing base publisher interface.
"""


from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar
from domain.events import BaseDomainEvent


E = TypeVar('E', bound=BaseDomainEvent)


class IBasePublisher(Generic[E], metaclass=ABCMeta):
    """
    IBasePublisher: Class, that represents base publisher interface for all publishers.
    It contains common abstract methods for every publisher.

    Args:
        Generic: Base class for base publisher interface that make this class template.
        ABCMeta: Base metaclass for base publisher interface that make this class abstract.
    """

    @abstractmethod
    async def publish(self, events: list[E]) -> None:
        """
        publish: Should call handlers for each domain event.
        Must be overriden.

        Args:
            events (list[E]): List of domain events.
        """

        pass
