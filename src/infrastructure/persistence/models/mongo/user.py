"""
user: File, containing twich user mongo dao.
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


class TwichUserDAO(BaseDAO):
    login: StringField = StringField(
        min_length=1,
        max_length=128,
        required=True,
        unique=True,
    )

    description: StringField = StringField(
        min_length=0,
        max_length=4096,
    )

    display_name: StringField = StringField(
        min_length=0,
        max_length=128,
    )

    type: StringField = StringField(
        min_length=0,
        max_length=128,
    )

    broadcaster_type: StringField = StringField(
        min_length=0,
        max_length=128,
    )

    profile_image_url: StringField = StringField(
        min_length=0,
        max_length=256,
    )

    offline_image_url: StringField = StringField(
        min_length=0,
        max_length=256,
    )

    created_at: DateTimeField = DateTimeField()

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
        'indexes': ['login'],
    }
