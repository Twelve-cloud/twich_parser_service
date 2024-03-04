"""
test_products_mapper.py: File, containing tests for product mapper.
"""


from datetime import datetime
from domain.entities.lamoda.product_entity import LamodaProduct
from infrastructure.mappers.lamoda.mongo.product_mapper import LamodaProductMapper
from infrastructure.models.lamoda.mongo.product_model import LamodaProduct


class TestLamodaProductMapper:
    def test_to_domain(self):
        persistence = LamodaProduct(
            sku='sku',
            url='url',
            category='category',
            description='description',
            price=0.0,
            price_currency='BYN',
            price_valid_until=datetime.utcnow(),
            parsed_at=datetime.utcnow(),
        )

        entity = LamodaProductMapper.to_domain(persistence)

        assert entity.sku == persistence.sku
        assert entity.parsed_at == persistence.parsed_at

    def test_to_persistence(self):
        entity = LamodaProduct(
            sku='sku',
            url='url',
            category='category',
            description='description',
            price=0.0,
            price_currency='BYN',
            price_valid_until=datetime.utcnow(),
            parsed_at=datetime.utcnow(),
        )

        persistence = LamodaProductMapper.to_persistence(entity)

        assert persistence.sku == entity.sku
        assert persistence.parsed_at == entity.parsed_at
