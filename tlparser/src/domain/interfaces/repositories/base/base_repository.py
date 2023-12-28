"""
base_repository.py: File, containing repository abstract class for every repository.
"""


from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar
from domain.entities.base.base_entity import BaseEntity
from domain.events.base.base_event import BaseDomainEvent
from domain.types.types import ResultWithEvent


T = TypeVar('T', bound=BaseEntity)
E = TypeVar('E', bound=BaseDomainEvent)


class IBaseRepository(Generic[T, E], metaclass=ABCMeta):
    """
    IBaseRepository: Abstract class for every repository.

    Args:
        Generic (_type_): Base superclass for IBaseRepository.
        metaclass (_type_): Base metaclass for IBaseRepository.
    """

    @abstractmethod
    async def create_or_update(self, entity: T) -> ResultWithEvent[T, E]:
        """
        create_or_update: Create entity in db if it does not exist, otherwise update it.

        Args:
            T (_type_): Entity.

        Returns:
            ResultWithEvent[T, E]: Result with domain event.
        """

        pass

    @abstractmethod
    async def all(self) -> list[T]:
        """
        all: Return list of entities. Must be overriden.

        Returns:
            list[T]: List of entities.
        """

        pass
