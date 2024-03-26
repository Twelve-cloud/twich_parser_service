"""
stream.py: File, containing parser interface for a twich stream.
"""


from abc import abstractmethod
from application.interfaces.parsers.base import IParser
from domain.models import TwichStream


class ITwichStreamParser(IParser):
    @abstractmethod
    async def parse_stream(self, user_login: str) -> TwichStream:
        raise NotImplementedError
