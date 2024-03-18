"""
game_model: File, containing twich game model for elastic search.
"""


from elasticsearch_dsl import Date, Document, Long, Text
from datetime import datetime


class TwichGameDAO(Document):
    """
    TwichGameDAO: Class, that represents twich game document in elastic database.

    Args:
        Document (_type_): Base superclass for TwichGameDAO class.
    """

    def __init__(
        self,
        id: int,
        name: str,
        igdb_id: str,
        box_art_url: str,
        parsed_at: datetime
    ) -> None:
        super().__init__(id=id, name=name, igdb_id=igdb_id, box_art_url=box_art_url, parsed_at=parsed_at)

    id: Long = Long()
    name: Text = Text()
    igdb_id: Text = Text()
    box_art_url: Text = Text()
    parsed_at: Date = Date(default_timezone='UTC')

    class Index:
        name: str = 'twich_game'
