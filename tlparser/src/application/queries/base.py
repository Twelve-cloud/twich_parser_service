"""
base.py: File, containing base query.
"""


from abc import ABC
from dataclasses import dataclass


@dataclass(frozen=True)
class Query(ABC):
    """
    Query: Class, representing base query. This class is abstract.
    All queries should be inherited from this class.
    You can create an instance of this class, but ABC shows that you should not do this.

    Bases:
        1) ABC: Abstract Base Class. It is a marker that this class should not be instantiated.
    """

    pass
