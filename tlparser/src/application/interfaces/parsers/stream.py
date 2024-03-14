"""
stream.py: File, containing parser interface for a twich stream.
"""


from abc import abstractmethod
from application.interfaces.parsers.base import IParser
from domain.models import TwichStream


class ITwichStreamParser(IParser):
    """
    ITwichStreamParser: Class, representing twich stream parser interface.
    This class is an interface.

    Bases:
        1) IParser: Base parser interface. Every parser should be inherited from this class.
    """

    @abstractmethod
    async def parse_stream(self, user_login: str) -> TwichStream:
        """
        parse_stream: Should parse stream.
        Must be overriden.

        Args:
            user_login (str): Login of the user.

        Raises:
            NotImplementedError: Raises to prevent calling this method by super.

        Returns:
            TwichStream: Twich stream domain model instance.
        """

        raise NotImplementedError
