"""
base_repository.py: File, containing repository abstract class for every repository.
"""


from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar
from domain.entities.base.base_entity import BaseEntity


T = TypeVar('T', bound=BaseEntity)


class BaseRepository(Generic[T], metaclass=ABCMeta):
    """
    BaseRepository: Abstract class for every repository.

    Args:
        Generic (_type_): Base superclass for BaseRepository.
        metaclass (_type_): Base metaclass for BaseRepository.
    """

    @abstractmethod
    def create_or_update(self, entity: T) -> T:
        """
        create_or_update: Create entity in db if it does not exist, otherwise update it.

        Args:
            T (_type_): Entity.

        Returns:
            entity (T): Created/Updated entity.
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
