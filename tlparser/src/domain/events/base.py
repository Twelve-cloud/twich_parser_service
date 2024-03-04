"""
base.py: File, containing base domain event.
"""


from dataclasses import dataclass


@dataclass
class BaseDomainEvent:
    """
    BaseDomainEvent: Class, that represents base domain event for all domain events.
    It contains common data for every domain event.
    """

    pass
