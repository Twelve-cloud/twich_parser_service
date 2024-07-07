"""
stream: File, containing twich stream mongo dao.
"""


from datetime import (
    datetime,
    timezone,
)

from mongoengine import (
    DateTimeField,
    IntField,
    ListField,
    StringField,
)

from infrastructure.persistence.models.mongo.base import BaseDAO


class TwichStreamDAO(BaseDAO):
    user_id: IntField = IntField(
        min_value=0,
    )

    user_name: StringField = StringField(
        min_length=1,
        max_length=128,
    )

    user_login: StringField = StringField(
        min_length=1,
        max_length=128,
    )

    game_id: IntField = IntField(
        min_value=0,
    )

    game_name: StringField = StringField(
        min_length=1,
        max_length=128,
    )

    language: StringField = StringField(
        min_length=0,
        max_length=128,
    )

    title: StringField = StringField(
        min_length=0,
        max_length=128,
    )

    tags: ListField = ListField(
        StringField(
            min_length=1,
            max_length=128,
        ),
    )

    started_at: DateTimeField = DateTimeField()

    viewer_count: IntField = IntField(
        min_value=0,
    )

    type: StringField = StringField(
        min_length=0,
        max_length=128,
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
        'indexes': ['user_login'],
    }
