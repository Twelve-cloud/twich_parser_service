"""
base_repository.py: File, containing repository abstract class for every repository.
"""


from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar
from domain.entities.base.base_entity import BaseEntity
from domain.events.base.base_event import BaseDomainEvent


T = TypeVar('T', bound=BaseEntity)
E = TypeVar('E', bound=BaseDomainEvent)


class ResultWithEvent(Generic[T, E]):
    """
    ResultWithEvent: Class, that contains result and event.

    Args:
        Generic (_type_): Base superclass for ResultWithEvent.
    """

    def __init__(self, result: T, event: E) -> None:
        """
        __init__: Initialize class with result and event.

        Args:
            result (T): Result.
            event (E): Event.
        """

        self.result = result
        self.event = event


class BaseRepository(Generic[T, E], metaclass=ABCMeta):
    """
    BaseRepository: Abstract class for every repository.

    Args:
        Generic (_type_): Base superclass for BaseRepository.
        metaclass (_type_): Base metaclass for BaseRepository.
    """

    @abstractmethod
    def create_or_update(self, entity: T) -> ResultWithEvent[T, E]:
        """
        create_or_update: Create entity in db if it does not exist, otherwise update it.

        Args:
            T (_type_): Entity.

        Returns:
            ResultWithEvent[T, E]: Result with domain event.
        """

        pass

    @abstractmethod
    def all(self) -> list[T]:
        """
        all: Return list of entities. Must be overriden.

        Returns:
            list[T]: List of entities.
        """

        pass
