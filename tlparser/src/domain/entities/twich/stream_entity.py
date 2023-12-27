"""
stream_entity.py: File, containing twich stream entity.
"""


from datetime import datetime
from typing import Optional
from domain.entities.base.base_entity import BaseEntity


class TwichStreamEntity(BaseEntity):
    """
    TwichStreamEntity: Class, representing twich stream entity.

    Args:
        BaseEntity (_type_): Base entity class.
    """

    def __init__(
        self,
        id: Optional[int] = None,
        user_id: Optional[int] = None,
        user_name: Optional[str] = None,
        user_login: Optional[str] = None,
        game_id: Optional[int] = None,
        game_name: Optional[str] = None,
        language: Optional[str] = None,
        title: Optional[str] = None,
        tags: Optional[list[str]] = None,
        started_at: Optional[datetime] = None,
        viewer_count: Optional[int] = None,
        type: Optional[str] = None,
        parsed_at: Optional[datetime] = None,
        **kwargs: dict,
    ) -> None:
        """
        __init__: Initialize twich stream entity.

        Args:
            id (Optional[int]): Identifier of the stream.
            user_id (Optional[str]): Identifier of the user who has started the stream.
            user_name (Optional[str]): Name of the user who has started the stream.
            user_login (Optional[str]): Login of the user who has started the stream.
            game_id (Optional[str]): Identifier of the game which has been streamed.
            game_name (Optional[str]): Name of the game which has been streamed.
            language (Optional[str]): Language of the stream.
            title (Optional[str]): Title of the stream.
            tags (Optional[list[str]]): Tags of the stream.
            started_at (Optional[datetime]): Date when stream has been started.
            viewer_count (Optional[int]): Number of viewers on the stream.
            type (Optional[str]): Type of the stream.
            parsed_at (Optional[datetime]): Parsing date of the stream.
        """

        super().__init__(parsed_at)

        self.id = id
        self.user_id = user_id
        self.user_name = user_name
        self.user_login = user_login
        self.game_id = game_id
        self.game_name = game_name
        self.language = language
        self.title = title
        self.tags = tags
        self.started_at = started_at
        self.viewer_count = viewer_count
        self.type = type
