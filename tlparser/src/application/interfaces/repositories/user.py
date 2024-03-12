"""
user.py: File, containing repository interface for a twich user.
"""


from abc import abstractmethod
from application.interfaces.repositories import IRepository
from domain.models import TwichUser


class ITwichUserRepository(IRepository[TwichUser]):
    @abstractmethod
    async def get_user_by_login(self, login: str) -> TwichUser:
        raise NotImplementedError
