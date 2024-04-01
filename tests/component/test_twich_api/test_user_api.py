"""
test_user_api.py: File, containing tests for twich user api.
"""


import pytest
from fastapi import status


pytestmark = pytest.mark.anyio


class TestTwichUserAPI:
    async def test_parse_twich_user(self, client):
        response = await client.post('/api/v1/twich/user/ilame')
        assert response.status_code == status.HTTP_200_OK

    async def test_private_parse_twich_user(self, client):
        response = await client.get('/api/v1/twich/private/user/ilame')
        assert response.status_code == status.HTTP_200_OK
        assert response.json().get('login') == 'ilame'

        response = await client.get('/api/v1/twich/private/user/3541231')
        assert response.status_code == status.HTTP_404_NOT_FOUND

    async def test_delete_twich_user_by_login(self, client):
        response = await client.delete('/api/v1/twich/user/ilame')
        assert response.status_code == status.HTTP_204_NO_CONTENT
