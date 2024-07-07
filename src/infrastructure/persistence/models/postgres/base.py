"""
base.py: File, containing base postgres dao.
"""


from uuid import (
    UUID,
    uuid4,
)

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)


class BaseDAO(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4,
    )
