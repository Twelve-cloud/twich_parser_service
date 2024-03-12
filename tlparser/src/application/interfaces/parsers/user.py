"""
user.py: File, containing parser interface for a twich user.
"""


from domain.interfaces.parsers import ITwichParser
from domain.models import TwichUser


class ITwichUserParser(ITwichParser):
    async def parse_user(self, login: str) -> TwichUser:
        pass
