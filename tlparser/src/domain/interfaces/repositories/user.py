"""
user.py: File, containing repository interface for a twich user.
"""


from abc import abstractmethod
from domain.interfaces.repositories import IBaseRepository
from domain.models import TwichUser


class ITwichUserRepository(IBaseRepository[TwichUser]):
    """
    ITwichUserRepository: Class that represents repository interface for a twich user.

    Args:
        IBaseRepository[TwichUser]: Base repository interface instantiated with twich user.
    """

    @abstractmethod
    async def get_user_by_login(self, login: str) -> TwichUser:
        """
        get_user_by_login: Should return user from a collection.
        Must be overriden.

        Args:
            login (str): Login of the user.

        Returns:
            TwichUser: Twich user domain model instance.
        """

        pass
