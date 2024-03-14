"""
user.py: File, containing parser interface for a twich user.
"""


from abc import abstractmethod
from application.interfaces.parsers.base import IParser
from domain.models import TwichUser


class ITwichUserParser(IParser):
    """
    ITwichUserParser: Class, representing twich user parser interface.
    This class is an interface.

    Bases:
        1) IParser: Base parser interface. Every parser should be inherited from this class.
    """

    @abstractmethod
    async def parse_user(self, login: str) -> TwichUser:
        """
        parse_user: Should parse user.
        Must be overriden.

        Args:
            login (str): Login of the user.

        Raises:
            NotImplementedError: Raises to prevent calling this method by super.

        Returns:
            TwichUser: Twich user domain model instance.
        """

        raise NotImplementedError
