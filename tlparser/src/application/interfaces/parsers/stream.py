"""
stream.py: File, containing parser interface for a twich stream.
"""


from abc import abstractmethod
from application.interfaces.parsers import ITwichParser
from domain.models import TwichStream


class ITwichStreamParser(ITwichParser):
    @abstractmethod
    async def parse_stream(self, user_login: str) -> TwichStream:
        raise NotImplementedError
