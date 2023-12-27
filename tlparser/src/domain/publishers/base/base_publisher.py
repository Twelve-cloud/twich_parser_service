"""
base_publisher.py: File, containing publisher abstract class for every publisher.
"""


from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar
from domain.events.base.base_event import BaseDomainEvent


T = TypeVar('T', bound=BaseDomainEvent)


class IBasePublisher(Generic[T], metaclass=ABCMeta):
    """
    IBasePublisher: Abstract class for every publisher.

    Args:
        Generic (_type_): Base superclass for IBasePublisher.
        metaclass (_type_): Base metaclass for IBasePublisher.
    """

    @abstractmethod
    def publish_created_or_updated_event(self, event: T) -> None:
        """
        publish_created_or_updated_event: Publish created or updated event.

        Args:
            T (_type_): Domain event.
        """

        pass
