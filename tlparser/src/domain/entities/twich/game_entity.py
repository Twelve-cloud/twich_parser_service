"""
game_entity.py: File, containing twich game entity.
"""


from datetime import datetime
from typing import Optional
from domain.entities.base.base_entity import BaseEntity


class TwichGameEntity(BaseEntity):
    """
    TwichGameEntity: Class, representing twich game entity.

    Args:
        BaseEntity (_type_): Base entity class.
    """

    def __init__(
        self,
        id: Optional[int] = None,
        name: Optional[str] = None,
        igdb_id: Optional[str] = None,
        box_art_url: Optional[str] = None,
        parsed_at: Optional[datetime] = None,
    ) -> None:
        """
        __init__: Initialize twich game entity.

        Args:
            id (Optional[int]): Identifier of the game.
            name (Optional[str]): Name of the game.
            igdb_id (Optional[str]): Igdb identifier of the game.
            box_art_url (Optional[str]): Url to game image.
            parsed_at (Optional[datetime]): Parsing date of the game.
        """

        super().__init__(parsed_at)

        self.id = id
        self.name = name
        self.igdb_id = igdb_id
        self.box_art_url = box_art_url
