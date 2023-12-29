"""
test_stream_api.py: File, containing tests for twich stream api.
"""


import pytest
from fastapi import status


pytestmark = pytest.mark.anyio


class TestTwichStreamAPI:
    async def test_parse_twich_stream(self, client):
        response = await client.post('/api/v1/twich/stream/stray228')
        assert response.status_code == status.HTTP_200_OK

    async def test_private_parse_twich_stream(self, client):
        response = await client.get('/api/v1/twich/private/stream/stray228')
        assert response.status_code == status.HTTP_200_OK or status.HTTP_404_NOT_FOUND

        response = await client.get('/api/v1/twich/private/stream/1232131')
        assert response.status_code == status.HTTP_404_NOT_FOUND

    async def test_delete_twich_stream_by_user_login(self, client):
        response = await client.delete('/api/v1/twich/stream/stray228')
        assert response.status_code == status.HTTP_204_NO_CONTENT
