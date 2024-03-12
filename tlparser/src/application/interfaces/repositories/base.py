"""
base.py: File, containing base repository interface.
"""


from interface import Interface
from typing import Generic, TypeVar
from domain.models import DomainModel


T = TypeVar('T', bound=DomainModel)


class IRepository(Generic[T], Interface):
    async def add_or_update(self, instance: T) -> None:
        pass

    async def delete(self, instance: T) -> None:
        pass

    async def all(self) -> list[T]:
        pass

    async def get_by_id(id: int) -> T:
        pass
