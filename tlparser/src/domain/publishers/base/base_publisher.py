"""
base_publisher.py: File, containing publisher abstract class for every publisher.
"""


from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar
from domain.events.base.base_event import BaseDomainEvent


T = TypeVar('T', bound=BaseDomainEvent)


class BasePublisher(Generic[T], metaclass=ABCMeta):
    """
    BasePublisher: Abstract class for every publisher.

    Args:
        Generic (_type_): Base superclass for BasePublisher.
        metaclass (_type_): Base metaclass for BasePublisher.
    """

    @abstractmethod
    def publish_created_or_updated_event(self, event: T) -> None:
        """
        publish_created_or_updated_event: Publish created or updated event.

        Args:
            T (_type_): Domain event.
        """

        pass
