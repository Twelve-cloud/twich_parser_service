"""
game_mapper.py: File, containing mapper for twich game.
"""


from domain.entities.twich.game_entity import TwichGameEntity
from presentation.schemas.twich.game_schema import TwichGameSchema


class TwichGameMapper:
    """
    TwichGameMapper: Class, that transform game schema to game domain model and vv.
    """

    @classmethod
    def to_domain(cls, schema: TwichGameSchema) -> TwichGameEntity:
        """
        to_domain: Transform twich game read schema to twich game domain model.

        Args:
            schema (TwichGameSchema): Twich game read schema instance.

        Returns:
            TwichGameEntity: Twich domain model instance.
        """

        return TwichGameEntity(**schema.model_dump())

    @classmethod
    def to_schema(cls, domain: TwichGameEntity) -> TwichGameSchema:
        """
        to_schema: Transform twich game domain model to twich game schema.

        Args:
            domain (TwichGameEntity): Twich game domain model instance.

        Returns:
            TwichGameSchema: Twich game read schema instance.
        """

        return TwichGameSchema.model_construct(
            id=domain.id,
            name=domain.name,
            igdb_id=domain.igdb_id,
            box_art_url=domain.box_art_url,
            parsed_at=domain.parsed_at,
        )
