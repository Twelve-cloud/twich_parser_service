"""
game.py: File, containing repository interface for a twich game.
"""


from abc import abstractmethod
from application.interfaces.repository.base import IRepository
from domain.models import TwichGame


class ITwichGameRepository(IRepository[TwichGame]):
    @abstractmethod
    async def get_game_by_name(self, name: str) -> TwichGame:
        raise NotImplementedError
