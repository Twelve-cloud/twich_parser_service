"""
test_user_mapper.py: File, containing tests for user mapper.
"""


from datetime import datetime
from domain.entities.twich.user_entity import TwichUserEntity
from infrastructure.mappers.twich.mongo.user_mapper import TwichUserMapper
from infrastructure.models.twich.mongo.user_model import TwichUser


class TestLamodaProductMapper:
    def test_to_domain(self):
        persistence = TwichUser(
            id=1,
            login='login',
            description='description',
            display_name='display_name',
            type='admin',
            broadcaster_type='affiliate',
            profile_image_url='profile_image_url',
            offline_image_url='offline_image_url',
            created_at=datetime.utcnow(),
            parsed_at=datetime.utcnow(),
        )

        entity = TwichUserMapper.to_domain(persistence)

        assert entity.id == persistence.id
        assert entity.parsed_at == persistence.parsed_at

    def test_to_persistence(self):
        entity = TwichUserEntity(
            id=1,
            login='login',
            description='description',
            display_name='display_name',
            type='admin',
            broadcaster_type='affiliate',
            profile_image_url='profile_image_url',
            offline_image_url='offline_image_url',
            created_at=datetime.utcnow(),
            parsed_at=datetime.utcnow(),
        )

        persistence = TwichUserMapper.to_persistence(entity)

        assert persistence.id == entity.id
        assert persistence.parsed_at == entity.parsed_at
