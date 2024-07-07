"""
game: File, containing twich game mongo dao.
"""


from datetime import (
    datetime,
    timezone,
)

from mongoengine import (
    DateTimeField,
    StringField,
)

from infrastructure.persistence.models.mongo.base import BaseDAO


class TwichGameDAO(BaseDAO):
    name: StringField = StringField(
        min_length=1,
        max_length=128,
        required=True,
        unique=True,
    )

    igdb_id: StringField = StringField(
        min_length=0,
        max_length=128,
    )

    box_art_url: StringField = StringField(
        min_length=0,
        max_length=256,
    )

    parsed_at: DateTimeField = DateTimeField(
        default=datetime.now(timezone.utc),
    )

    meta: dict = {
        'ordering': ['-parsed_at'],
        'index_opts': {},
        'index_background': True,
        'index_cls': False,
        'auto_create_index': True,
        'auto_create_index_on_save': False,
        'indexes': ['name'],
    }
