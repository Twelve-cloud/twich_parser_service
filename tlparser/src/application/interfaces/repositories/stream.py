"""
stream.py: File, containing repository interface for a twich stream.
"""


from domain.interfaces.repositories import IRepository
from domain.models import TwichStream


class ITwichStreamRepository(IRepository[TwichStream]):
    async def get_stream_by_user_login(self, user_login: str) -> TwichStream:
        pass
