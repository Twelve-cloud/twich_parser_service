"""
user_model: File, containing twich user model for elastic search.
"""


from elasticsearch_dsl import Date, Document, Long, Text


class TwichUser(Document):
    """
    TwichUser: Class, that represents twich user document in mongo database.

    Args:
        Document (_type_): Base superclass for TwichUser class.
    """

    id: Long = Long()
    login: Text = Text()
    description: Text = Text()
    display_name: Text = Text()
    type: Text = Text()
    broadcaster_type: Text = Text()
    profile_image_url: Text = Text()
    offline_image_url: Text = Text()
    created_at: Date = Date(default_timezone='UTC')
    parsed_at: Date = Date(default_timezone='UTC')

    class Index:
        name: str = 'twich_user'
