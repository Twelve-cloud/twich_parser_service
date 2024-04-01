"""
test_game_mapper.py: File, containing tests for game mapper.
"""


from datetime import datetime

from application.dtos.fastapi_schemas.twich.game_schema import TwichGameSchema
from application.mappers.twich.game_mapper import TwichGameMapper
from domain.entities.twich.game_entity import TwichGameEntity


class TestLamodaProductMapper:
    def test_to_domain(self):
        schema = TwichGameSchema(
            id=1,
            name='name',
            igdb_id='igdb_id',
            box_art_url='box_art_url',
            parsed_at=datetime.utcnow(),
        )

        entity = TwichGameMapper.to_domain(schema)

        assert entity.id == schema.id
        assert entity.parsed_at == schema.parsed_at

    def test_to_schema(self):
        entity = TwichGameEntity(
            id=1,
            name='name',
            igdb_id='igdb_id',
            box_art_url='box_art_url',
            parsed_at=datetime.utcnow(),
        )

        schema = TwichGameMapper.to_schema(entity)

        assert schema.id == entity.id
        assert schema.parsed_at == entity.parsed_at
