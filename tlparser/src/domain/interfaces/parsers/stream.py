"""
stream.py: File, containing parser interface for a twich stream.
"""


from abc import abstractmethod
from domain.interfaces.parsers import ITwichBaseParser
from domain.models import TwichStream


class ITwichStreamParser(ITwichBaseParser):
    """
    ITwichStreamParser: Class that represents parser interface for a twich stream.

    Args:
        ITwichBaseParser: Base twich parser interface.
    """

    @abstractmethod
    async def parse_stream(self, user_login: str) -> TwichStream:
        """
        parse_stream: Parse stream data from the Twich, then create it and return.

        Args:
            user_login (str): Login of the user.

        Returns:
            TwichStream: Twich stream domain model instance.
        """

        pass
