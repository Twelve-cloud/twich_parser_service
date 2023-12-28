"""
test_game_mapper.py: File, containing tests for game mapper.
"""


from datetime import datetime
from domain.entities.twich.game_entity import TwichGameEntity
from infrastructure.mappers.twich.mongo.game_mapper import TwichGameMapper
from infrastructure.models.twich.mongo.game_model import TwichGame


class TestLamodaProductMapper:
    def test_to_domain(self):
        persistence = TwichGame(
            id=1,
            name='name',
            igdb_id='igdb_id',
            box_art_url='box_art_url',
            parsed_at=datetime.utcnow(),
        )

        entity = TwichGameMapper.to_domain(persistence)

        assert entity.id == persistence.id
        assert entity.parsed_at == persistence.parsed_at

    def test_to_persistence(self):
        entity = TwichGameEntity(
            id=1,
            name='name',
            igdb_id='igdb_id',
            box_art_url='box_art_url',
            parsed_at=datetime.utcnow(),
        )

        persistence = TwichGameMapper.to_persistence(entity)

        assert persistence.id == entity.id
        assert persistence.parsed_at == entity.parsed_at
