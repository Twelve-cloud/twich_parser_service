"""
base.py: File, containing base repository interface.
"""


from abc import ABC as Interface
from abc import abstractmethod
from typing import Generic, TypeVar
from domain.models import DomainModel


T = TypeVar('T', bound=DomainModel)


class IRepository(Interface, Generic[T]):
    @abstractmethod
    async def add_or_update(self, instance: T) -> None:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, instance: T) -> None:
        raise NotImplementedError

    @abstractmethod
    async def all(self) -> list[T]:
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, id: int) -> T:
        raise NotImplementedError
