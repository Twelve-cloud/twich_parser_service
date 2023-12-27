"""
base_service.py: File, containing base service for every service abstract class.
"""


from abc import ABCMeta
from typing import Generic, TypeVar
from domain.entities.base.base_entity import BaseEntity


T = TypeVar('T', bound=BaseEntity)


class IBaseService(Generic[T], metaclass=ABCMeta):
    """
    BaseService: Class, that represents base service for every serivce abstract class.

    Args:
        Generic (_type_): Base superclass for BaseService.
        metaclass (_type_): Base metaclass for BaseService.
    """

    pass
