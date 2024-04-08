"""
user_model: File, containing twich user model for mongo.
"""


from datetime import datetime

from mongoengine import (
    DateTimeField,
    Document,
    IntField,
    StringField,
)


class TwichUserDAO(Document):
    """
    TwichUserDAO: Class, that represents twich user document in mongo database.

    Args:
        Document (_type_): Base superclass for TwichUserDAO class.
    """

    id: IntField = IntField(
        min_value=0,
        primary_key=True,
    )

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
        default=datetime.utcnow,
    )

    meta: dict = {
        'ordering': ['-parsed_at'],
        'index_opts': {},
        'index_background': True,
        'index_cls': False,
        'auto_create_index': True,
        'auto_create_index_on_save': False,
        'indexes': ['login', 'display_name'],
    }
