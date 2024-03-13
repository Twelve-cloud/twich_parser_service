"""
common.py: File, containing common things related to domain events.
"""


from typing import TypeVar
from domain.events.base import DomainEvent


DE = TypeVar('DE', bound=DomainEvent)
