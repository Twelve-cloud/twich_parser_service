"""
game.py: File, containing repository interface for a twich game.
"""


from domain.interfaces.repositories import IRepository
from domain.models import TwichGame


class ITwichGameRepository(IRepository[TwichGame]):
    async def get_game_by_name(self, name: str) -> TwichGame:
        pass
