"""
base_entity.py: File, containing base entity for every entity.
"""


from datetime import datetime
from typing import Optional


class BaseEntity:
    """
    BaseEntity: Class, representing base entity.
    """

    def __init__(self, parsed_at: Optional[datetime] = None) -> None:
        """
        __init__: Initialize base entity.

        Args:
            parsed_at (Optional[datetime]): Parsing date of the entity.
        """

        self.parsed_at = parsed_at
