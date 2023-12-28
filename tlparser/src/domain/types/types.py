"""
types.py: File, containing special types to work with domain.
"""


from typing import Generic, TypeVar
from domain.entities.base.base_entity import BaseEntity
from domain.events.base.base_event import BaseDomainEvent


T = TypeVar('T', bound=BaseEntity)
E = TypeVar('E', bound=BaseDomainEvent)


class ResultWithEvent(Generic[T, E]):
    """
    ResultWithEvent: Class, that contains result and event.

    Args:
        Generic (_type_): Base superclass for ResultWithEvent.
    """

    def __init__(self, result: T, event: E) -> None:
        """
        __init__: Initialize class with result and event.

        Args:
            result (T): Result.
            event (E): Event.
        """

        self.result = result
        self.event = event
