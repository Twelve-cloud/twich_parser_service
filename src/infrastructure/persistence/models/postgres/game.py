"""
game: File, containing twich game postgres dao.
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


class TwichGameDAO(BaseDAO):
    name: Mapped[str] = mapped_column(
        String(128),
        unique=True,
        index=True,
    )

    igdb_id: Mapped[str] = mapped_column(
        String(128),
    )

    box_art_url: Mapped[str] = mapped_column(
        String(256),
    )

    parsed_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now(timezone.utc),
    )
