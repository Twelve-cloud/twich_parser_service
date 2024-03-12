"""
base.py: File, containing base repository interface.
"""


from typing import Generic, TypeVar
from interface import Interface
from domain.models import DomainModel


T = TypeVar('T', bound=DomainModel)


class IRepository(Generic[T], Interface):
    async def add_or_update(self, instance: T) -> None:
        raise NotImplementedError

    async def delete(self, instance: T) -> None:
        raise NotImplementedError

    async def all(self) -> list[T]:
        raise NotImplementedError

    async def get_by_id(id: int) -> T:
        raise NotImplementedError
