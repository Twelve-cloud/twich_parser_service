"""
base.py: File, containing base repository interface.
"""


from abc import ABC as Interface
from abc import abstractmethod
from typing import Generic
from domain.models import DM


class IRepository(Interface, Generic[DM]):
    """
    IRepository: Class, representing repository interface. This class is an interface.
    You can create an instance of this class, but Interface shows that you should not do this.
    Interface base class is Abstract Base Class. It is called Interface to make intention explicit.

    Bases:
        1) Interface: Abstract Base Class. It is a marker that this class provides interface only.
        2) Generic[DM]: Generic class. This class makes repository interface generic.
    """

    @abstractmethod
    async def add_or_update(self, instance: DM) -> None:
        """
        add_or_update: Should add or update domain model instance.
        Must be overriden.

        Args:
            instance (DM): Domain model instance.

        Raises:
            NotImplementedError: Raises to prevent calling this method by super.
        """

        raise NotImplementedError

    @abstractmethod
    async def delete(self, instance: DM) -> None:
        """
        delete: Should delete domain model instance.
        Must be overriden.

        Args:
            instance (DM): Domain model instance.

        Raises:
            NotImplementedError: Raises to prevent calling this method by super.
        """

        raise NotImplementedError

    @abstractmethod
    async def all(self) -> list[DM]:
        """
        all: Should return all domain model instances.
        Must be overriden.

        Raises:
            NotImplementedError: Raises to prevent calling this method by super.

        Returns:
            list[DM]: List of domain model instances.
        """

        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, id: int) -> DM:
        """
        get_by_id: Should return domain model instance by its id.
        Must be overriden.

        Args:
            id (int): ID of the domain model instance.

        Raises:
            NotImplementedError: Raises to prevent calling this method by super.

        Returns:
            DM: Domain model instance.
        """

        raise NotImplementedError
