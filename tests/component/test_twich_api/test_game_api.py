"""
test_game_api.py: File, containing tests for twich game api.
"""


import pytest
from fastapi import status


pytestmark = pytest.mark.anyio


class TestTwichGameAPI:
    async def test_parse_twich_game(self, client):
        response = await client.post('/api/v1/twich/game/valorant')
        assert response.status_code == status.HTTP_200_OK

    async def test_private_parse_twich_game(self, client):
        response = await client.get('/api/v1/twich/private/game/valorant')
        assert response.status_code == status.HTTP_200_OK
        assert response.json().get('name') == 'VALORANT'

        response = await client.get('/api/v1/twich/private/game/valorant1')
        assert response.status_code == status.HTTP_404_NOT_FOUND

    async def test_delete_twich_game_by_name(self, client):
        response = await client.delete('/api/v1/twich/game/valorant')
        assert response.status_code == status.HTTP_204_NO_CONTENT
