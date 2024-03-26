"""
stream.py: File, containing repository interface for a twich stream.
"""


from abc import abstractmethod
from application.interfaces.repository.base import IRepository
from domain.models import TwichStream


class ITwichStreamRepository(IRepository[TwichStream]):
    @abstractmethod
    async def get_stream_by_user_login(self, user_login: str) -> TwichStream:
        raise NotImplementedError
