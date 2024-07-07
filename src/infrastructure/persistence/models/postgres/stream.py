"""
stream.py: File, containing twich stream postgres dao.
"""


from datetime import (
    datetime,
    timezone,
)

from sqlalchemy import (
    ARRAY,
    DateTime,
    Integer,
    String,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from infrastructure.persistence.models.postgres.base import BaseDAO


class TwichStreamDAO(BaseDAO):
    user_id: Mapped[int] = mapped_column(
        Integer(),
    )

    user_name: Mapped[str] = mapped_column(
        String(128),
    )

    user_login: Mapped[str] = mapped_column(
        String(128),
        index=True,
    )

    game_id: Mapped[int] = mapped_column(
        Integer(),
    )

    game_name: Mapped[str] = mapped_column(
        String(128),
    )

    language: Mapped[str] = mapped_column(
        String(128),
    )

    title: Mapped[str] = mapped_column(
        String(128),
    )

    tags: Mapped[ARRAY] = ARRAY(
        String(128),
    )

    started_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
    )

    viewer_count: Mapped[int] = mapped_column(
        Integer(),
    )

    type: Mapped[str] = mapped_column(
        String(128),
    )

    parsed_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now(timezone.utc),
    )
