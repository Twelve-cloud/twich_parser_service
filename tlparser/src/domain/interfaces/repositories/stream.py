"""
stream.py: File, containing repository interface for a twich stream.
"""


from abc import abstractmethod
from domain.interfaces.repositories import IBaseRepository
from domain.models import TwichStream


class ITwichStreamRepository(IBaseRepository[TwichStream]):
    """
    ITwichStreamRepository: Class that represents repository interface for a twich stream.

    Args:
        IBaseRepository[TwichStream]: Base repository interface instantiated with twich stream.
    """

    @abstractmethod
    async def get_stream_by_user_login(self, user_login: str) -> TwichStream:
        """
        get_stream_by_user_login: Should return stream from a collection.
        Must be overriden.

        Args:
            user_login (str): Login of the user.

        Returns:
            TwichStream: Twich stream domain model instance.
        """

        pass
