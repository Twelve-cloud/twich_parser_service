"""
user.py: File, containing twich user postgres dao.
"""


from datetime import (
    datetime,
    timezone,
)

from sqlalchemy import (
    DateTime,
    String,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from infrastructure.persistence.models.postgres.base import BaseDAO


class TwichUserDAO(BaseDAO):
    login: Mapped[str] = mapped_column(
        String(128),
        unique=True,
    )

    description: Mapped[str] = mapped_column(
        String(4096),
    )

    display_name: Mapped[str] = mapped_column(
        String(128),
    )

    type: Mapped[str] = mapped_column(
        String(128),
    )

    broadcaster_type: Mapped[str] = mapped_column(
        String(128),
    )

    profile_image_url: Mapped[str] = mapped_column(
        String(256),
    )

    offline_image_url: Mapped[str] = mapped_column(
        String(256),
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
    )

    parsed_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now(timezone.utc),
    )
