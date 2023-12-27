"""
product_model: File, containing lamoda product model for mongo.
"""


from datetime import datetime
from mongoengine import DateTimeField, Document, FloatField, StringField


class LamodaProduct(Document):
    """
    LamodaProduct: Class, that represents lamoda product document in mongo database.

    Args:
        Document (_type_): Base superclass for LamodaProduct class.
    """

    sku: StringField = StringField(
        min_length=1,
        max_length=128,
        primary_key=True,
    )

    url: StringField = StringField(
        min_length=1,
        max_length=256,
        required=True,
        unique=True,
    )

    category: StringField = StringField(
        min_length=1,
        max_length=128,
        required=True,
    )

    description: StringField = StringField(
        min_length=0,
        max_length=4096,
    )

    price: FloatField = FloatField(
        min_value=0,
    )

    price_currency: StringField = StringField(
        min_length=0,
        max_length=128,
    )

    price_valid_until: DateTimeField = DateTimeField()

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
        'indexes': ['url', 'category'],
    }
