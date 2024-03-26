"""
user.py: File, containing parser interface for a twich user.
"""


from abc import abstractmethod
from application.interfaces.parsers.base import IParser
from domain.models import TwichUser


class ITwichUserParser(IParser):
    @abstractmethod
    async def parse_user(self, login: str) -> TwichUser:
        raise NotImplementedError
