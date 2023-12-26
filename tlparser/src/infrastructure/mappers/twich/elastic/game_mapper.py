"""
game_mapper.py: File, containig twich game mapper.
"""


from domain.entities.twich.game_entity import TwichGameEntity
from infrastructure.models.twich.elastic.game_model import TwichGame


class TwichGameMapper:
    """
    TwichGameMapper: Class, representing twich game mapper.
    """

    @classmethod
    def to_domain(self, persistence: TwichGame) -> TwichGameEntity:
        """
        to_domain: Transform persistence game model to domain game model.

        Args:
            persistence (TwichGame): Persistence game model.

        Returns:
            TwichGameEntity: Domain game model.
        """

        return TwichGameEntity(
            id=persistence.id,
            name=persistence.name,
            igdb_id=persistence.igdb_id,
            box_art_url=persistence.box_art_url,
            parsed_at=persistence.parsed_at,
        )

    @classmethod
    def to_persistence(self, domain: TwichGameEntity) -> TwichGame:
        """
        to_persistence: Transform domain game model to persistence game model.

        Args:
            domain (TwichGameEntity): Domain game model.

        Returns:
            TwichGame: Persistence game model.
        """

        return TwichGame(
            id=domain.id,
            name=domain.name,
            igdb_id=domain.igdb_id,
            box_art_url=domain.box_art_url,
            parsed_at=domain.parsed_at,
        )
