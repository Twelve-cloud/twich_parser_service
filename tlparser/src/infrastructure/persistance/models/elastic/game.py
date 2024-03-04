"""
game_model: File, containing twich game model for elastic search.
"""


from elasticsearch_dsl import Date, Document, Long, Text


class TwichGameDAO(Document):
    """
    TwichGameDAO: Class, that represents twich game document in elastic database.

    Args:
        Document (_type_): Base superclass for TwichGameDAO class.
    """

    id: Long = Long()
    name: Text = Text()
    igdb_id: Text = Text()
    box_art_url: Text = Text()
    parsed_at: Date = Date(default_timezone='UTC')

    class Index:
        name: str = 'twich_game'
