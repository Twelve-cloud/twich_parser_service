"""
base.py: File, containing base dto.
"""


from abc import ABC
from dataclasses import dataclass


@dataclass(frozen=True)
class DTO(ABC):
    """
    DTO: Class, representing base DTO. This class is abstract.
    All DTO should be inherited from this class.
    You can create an instance of this class, but ABC shows that you should not do this.

    Bases:
        1) ABC: Abstract Base Class. It is a marker that this class should not be instantiated.
    """

    pass
