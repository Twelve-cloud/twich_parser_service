"""
base.py: File, containing base mongo dao.
"""


from uuid import (
    uuid4,
)

from mongoengine import (
    Document,
    UUIDField,
)


class BaseDAO(Document):
    id: UUIDField = UUIDField(
        default=uuid4,
    )
