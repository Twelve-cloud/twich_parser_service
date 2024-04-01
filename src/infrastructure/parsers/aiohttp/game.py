"""
game.py: File, containing parser for a twich game.
"""


from datetime import datetime
from typing import Optional
from aiohttp import ClientSession
from application.exceptions import (
    ObjectNotFoundException,
    TwichGetObjectBadRequestException,
    TwichRequestUnauthorizedException,
)
from shared.config import settings
from domain.models import TwichGame
from infrastructure.parsers.aiohttp.dependencies import TwichAPIToken


class TwichGameParser:
    def __init__(self, token: TwichAPIToken) -> None:
        self.token: TwichAPIToken = token

    async def parse_game(self, name: str) -> TwichGame:
        async with ClientSession() as session:
            async with session.get(
                f'{settings.TWICH_GET_GAME_BASE_URL}?name={name}',
                headers=self.token.headers,
                timeout=10,
            ) as response:
                if response.status == 400:
                    raise TwichGetObjectBadRequestException('Get game bad request to Twich API')

                if response.status == 401:
                    raise TwichRequestUnauthorizedException('Request to Twich API is unauthorized.')

                game_json: Optional[dict] = await response.json()

                if not game_json:
                    raise ObjectNotFoundException('Game is not found.')

                game_data: Optional[list] = game_json.get('data')

                if not game_data:
                    raise ObjectNotFoundException('Game is not found.')

                game: TwichGame = TwichGame.create(
                    **game_data[0],
                    parsed_at=datetime.utcnow(),
                )

                return game
