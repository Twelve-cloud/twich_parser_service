"""
base.py: File, containing base service interface.
"""


from abc import ABCMeta


class IBaseService(metaclass=ABCMeta):
    """
    IBaseService: Class, that represents base service interface for all services.
    It contains common abstract methods for every service.

    Args:
        ABCMeta: Base metaclass for base service interface that make this class abstract.
    """

    pass
