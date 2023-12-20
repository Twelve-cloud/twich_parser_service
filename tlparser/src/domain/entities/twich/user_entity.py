"""
user_entity.py: File, containing twich user entity.
"""


from datetime import datetime
from typing import Optional
from domain.entities.base.base_entity import BaseEntity


class TwichUserEntity(BaseEntity):
    """
    TwichUserEntity: Class, representing twich user entity.

    Args:
        BaseEntity (_type_): Base entity class.
    """

    def __init__(
        self,
        id: Optional[int] = None,
        login: Optional[str] = None,
        description: Optional[str] = None,
        display_name: Optional[str] = None,
        type: Optional[str] = None,
        broadcaster_type: Optional[str] = None,
        profile_image_url: Optional[str] = None,
        offline_image_url: Optional[str] = None,
        created_at: Optional[datetime] = None,
        parsed_at: Optional[datetime] = None,
    ) -> None:
        """
        __init__: Initialize twich user entity.

        Args:
            id (Optional[int]): Identifier of the user.
            login (Optional[str]): Login of the user.
            description (Optional[str]): Description of the user.
            display_name (Optional[str]): Display name of the user.
            type (Optional[str]): Type of the user.
            broadcaster_type (Optional[str]): Broadcaster type of the user.
            profile_image_url (Optional[str]): Profile image url of the user.
            offline_image_url (Optional[str]): Offline image url of the user.
            created_at (Optional[datetime]): Creation date of the user.
            parsed_at (Optional[datetime]): Parsing date of the user.
        """

        super().__init__(parsed_at)

        self.id = id
        self.login = login
        self.description = description
        self.display_name = display_name
        self.type = type
        self.broadcaster_type = broadcaster_type
        self.profile_image_url = profile_image_url
        self.offline_image_url = offline_image_url
        self.created_at = created_at
