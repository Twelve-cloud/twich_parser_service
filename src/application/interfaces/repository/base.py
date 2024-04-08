"""
base.py: File, containing base repository interface.
"""


from abc import ABC as Interface
from abc import abstractmethod
from typing import Generic

from domain.models import DM


class IRepository(Interface, Generic[DM]):
    @abstractmethod
    async def add_or_update(self, instance: DM) -> None:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, instance: DM) -> None:
        raise NotImplementedError

    @abstractmethod
    async def all(self) -> list[DM]:
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, id: int) -> DM:
        raise NotImplementedError
