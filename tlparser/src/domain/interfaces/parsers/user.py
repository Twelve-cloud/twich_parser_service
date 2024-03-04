"""
user.py: File, containing parser interface for a twich user.
"""


from abc import abstractmethod
from domain.interfaces.parsers import ITwichBaseParser
from domain.models import TwichUser


class ITwichUserParser(ITwichBaseParser):
    """
    ITwichUserParser: Class that represents parser interface for a twich user.

    Args:
        ITwichBaseParser: Base twich parser interface.
    """

    @abstractmethod
    async def parse_user(self, login: str) -> TwichUser:
        """
        parse_user: Parse user data from the Twich, then create it and return.

        Args:
            login (str): Login of the user.

        Returns:
            TwichUser: Twich user domain model instance.
        """

        pass
