"""
game_model: File, containing twich game model for mongo.
"""


from datetime import datetime
from mongoengine import DateTimeField, Document, IntField, StringField


class TwichGameDAO(Document):
    """
    TwichGameDAO: Class, that represents twich game document in mongo database.

    Args:
        Document (_type_): Base superclass for TwichGameDAO class.
    """

    id: IntField = IntField(
        min_value=0,
        primary_key=True,
    )

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
        default=datetime.utcnow,
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
