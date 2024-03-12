"""
user.py: File, containing parser interface for a twich user.
"""


from abc import abstractmethod
from application.interfaces.parsers import ITwichParser
from domain.models import TwichUser


class ITwichUserParser(ITwichParser):
    @abstractmethod
    async def parse_user(self, login: str) -> TwichUser:
        raise NotImplementedError
