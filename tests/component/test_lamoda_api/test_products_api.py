"""
test_products_api.py: File, containing tests for lamoda products api.
"""


import pytest
from fastapi import status


pytestmark = pytest.mark.anyio


class TestLamodaProductsAPI:
    async def test_parse_lamoda_products(self, client):
        response = await client.post('/api/v1/lamoda/products/1480')
        assert response.status_code == status.HTTP_200_OK

    async def test_private_parse_lamoda_products(self, client):
        response = await client.get('/api/v1/lamoda/products/1480')
        assert response.status_code == status.HTTP_200_OK

        response = await client.get('/api/v1/lamoda/private/products/1232131')
        assert response.status_code == status.HTTP_404_NOT_FOUND

    async def test_delete_lamoda_products_by_category(self, client):
        response = await client.delete('/api/v1/lamoda/products/Обложки для документов')
        assert response.status_code == status.HTTP_204_NO_CONTENT
