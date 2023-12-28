"""
base_service.py: File, containing base service for every service abstract class.
"""


from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar
from application.schemas.base.base_schema import BaseROSchema


T = TypeVar('T', bound=BaseROSchema)


class IBaseService(Generic[T], metaclass=ABCMeta):
    """
    BaseService: Class, that represents base service for every serivce abstract class.

    Args:
        Generic (_type_): Base superclass for BaseService.
        metaclass (_type_): Base metaclass for BaseService.
    """

    @abstractmethod
    async def create(self, schema: T) -> None:
        """
        create: Create entity.

        Args:
            schema (T): Entity schema.
        """

        pass
