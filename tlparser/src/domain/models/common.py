"""
common.py: File, containing common things related to domain models.
"""


from typing import TypeVar
from domain.models.base import DomainModel


DM = TypeVar('DM', bound=DomainModel)
