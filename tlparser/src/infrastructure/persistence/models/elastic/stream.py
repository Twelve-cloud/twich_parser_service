"""
stream_model: File, containing twich stream model for elastic search.
"""


from elasticsearch_dsl import Date, Document, InnerDoc, Integer, Long, Nested, Text


class Tag(InnerDoc):
    """
    Tag: Class, that represents twich stream tag.

    Args:
        InnerDoc (_type_): Base superclass for Tag class.
    """

    tag: Text = Text()


class TwichStreamDAO(Document):
    """
    TwichStreamDAO: Class, that represents twich stream document in mongo database.

    Args:
        Document (_type_): Base superclass for TwichStreamDAO class.
    """

    id: Long = Long()
    user_id: Integer = Integer()
    user_name: Text = Text()
    user_login: Text = Text()
    game_id: Integer = Integer()
    game_name: Text = Text()
    language: Text = Text()
    title: Text = Text()
    tags: Nested = Nested(Tag)
    started_at: Date = Date(default_timezone='UTC')
    viewer_count: Integer = Integer()
    type: Text = Text()
    parsed_at: Date = Date(default_timezone='UTC')

    class Index:
        name: str = 'twich_stream'
