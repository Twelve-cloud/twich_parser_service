"""
game_mapper.py: File, containing mapper for twich game.
"""


from application.schemas.twich.game_schema import TwichGameCreateSchema, TwichGameReadSchema
from domain.entities.twich.game_entity import TwichGameEntity


class TwichGameCreateMapper:
    """
    TwichGameCreateMapper: Class, that transform game schema to game domain model and vv.
    """

    @classmethod
    def to_domain(cls, schema: TwichGameCreateSchema) -> TwichGameEntity:
        """
        to_domain: Transform twich game create schema to twich game domain model.

        Args:
            schema (TwichGameCreateSchema): Twich game create schema instance.

        Returns:
            TwichGameEntity: Twich domain model instance.
        """

        return TwichGameEntity(**schema.model_dump())

    @classmethod
    def to_schema(cls, domain: TwichGameEntity) -> TwichGameCreateSchema:
        """
        to_schema: Transform twich game domain model to twich game create schema.

        Args:
            domain (TwichGameEntity): Twich game domain model instance.

        Returns:
            TwichGameCreateSchema: Twich game create schema instance.
        """

        return TwichGameCreateSchema.model_construct(
            id=domain.id,
            name=domain.name,
            igdb_id=domain.igdb_id,
            box_art_url=domain.box_art_url,
        )


class TwichGameReadMapper:
    """
    TwichGameReadMapper: Class, that transform game schema to game domain model and vv.
    """

    @classmethod
    def to_domain(cls, schema: TwichGameReadSchema) -> TwichGameEntity:
        """
        to_domain: Transform twich game read schema to twich game domain model.

        Args:
            schema (TwichGameReadSchema): Twich game read schema instance.

        Returns:
            TwichGameEntity: Twich domain model instance.
        """

        return TwichGameEntity(**schema.model_dump())

    @classmethod
    def to_schema(cls, domain: TwichGameEntity) -> TwichGameReadSchema:
        """
        to_schema: Transform twich game domain model to twich game schema.

        Args:
            domain (TwichGameEntity): Twich game domain model instance.

        Returns:
            TwichGameReadSchema: Twich game read schema instance.
        """

        return TwichGameReadSchema.model_construct(
            id=domain.id,
            name=domain.name,
            igdb_id=domain.igdb_id,
            box_art_url=domain.box_art_url,
            parsed_at=domain.parsed_at,
        )
