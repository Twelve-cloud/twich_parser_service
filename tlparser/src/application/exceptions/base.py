"""
base.py: File, containing base application exception.
"""


from abc import ABC
from dataclasses import dataclass


@dataclass(frozen=True)
class ApplicationException(Exception, ABC):
    """
    ApplicationException: Class, representing base application exception. This class is abstract.
    All application exceptions should be inherited from this class.
    You can create an instance of this class, but ABC shows that you should not do this.

    Bases:
        1) Exception: Base exception class.
        2) ABC: Abstract Base Class. It is a marker that this class should not be instantiated.
    """

    message: str
