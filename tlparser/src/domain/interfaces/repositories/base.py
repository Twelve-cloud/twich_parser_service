"""
base.py: File, containing base repository interface.
"""


from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar
from domain.models import BaseDomainModel


T = TypeVar('T', bound=BaseDomainModel)


class IBaseRepository(Generic[T], metaclass=ABCMeta):
    """
    IBaseRepository: Class, that represents base repository interface for all repositories.
    It contains common abstract methods for every repository.

    Args:
        Generic: Base class for base repository interface that make this class template.
        ABCMeta: Base metaclass for base repository interface that make this class abstract.
    """

    @abstractmethod
    async def add_or_update(self, instance: T) -> None:
        """
        add_or_update: Should add instance to collection if it does not exist, otherwise update it.
        Must be overriden.

        Args:
            instance (T): Instance that should be added/updated.
        """

        pass

    @abstractmethod
    async def delete(self, instance: T) -> None:
        """
        delete_game_by_name: Should delete instance from a collection.
        Must be overriden.

        Args:
            instance (T): Instance that should be deleted.
        """

        pass

    @abstractmethod
    async def all(self) -> list[T]:
        """
        all: Should return list of all instances from collection.
        Must be overriden.

        Returns:
            list[T]: List of all instances from collection.
        """

        pass
