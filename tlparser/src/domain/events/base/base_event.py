"""
base_event.py: File, containing base domain event.
"""


from abc import ABCMeta


class BaseDomainEvent(metaclass=ABCMeta):
    """
    BaseDomainEvent: Class, that represents base domain event.

    Args:
        metaclass (_type_, optional): Metaclass, that makes base domain event class as abstract.
    """

    pass
