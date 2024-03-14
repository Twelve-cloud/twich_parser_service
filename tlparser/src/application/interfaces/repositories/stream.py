"""
stream.py: File, containing repository interface for a twich stream.
"""


from abc import abstractmethod
from application.interfaces.repositories.base import IRepository
from domain.models import TwichStream


class ITwichStreamRepository(IRepository[TwichStream]):
    """
    ITwichStreamRepository: Class, representing twich stream repository interface.
    This class is an interface.

    Bases:
        1) IRepository[TwichStream]: Base repository interface.
           Every repository should be inherited from this class.
    """

    @abstractmethod
    async def get_stream_by_user_login(self, user_login: str) -> TwichStream:
        """
        get_stream_by_user_login: Should return twich stream model instance by its user login.

        Args:
            user_login (str): Login of the user.

        Raises:
            NotImplementedError: Raises to prevent calling this method by super.

        Returns:
            TwichStream: Twich stream domain model instance.
        """

        raise NotImplementedError
