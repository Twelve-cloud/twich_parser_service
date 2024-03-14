"""
user.py: File, containing repository interface for a twich user.
"""


from abc import abstractmethod
from application.interfaces.repositories.base import IRepository
from domain.models import TwichUser


class ITwichUserRepository(IRepository[TwichUser]):
    """
    ITwichUserRepository: Class, representing twich user repository interface.
    This class is an interface.

    Bases:
        1) IRepository[TwichUser]: Base repository interface.
           Every repository should be inherited from this class.
    """

    @abstractmethod
    async def get_user_by_login(self, login: str) -> TwichUser:
        """
        get_user_by_login: Should return twich user model instance by its login.
        Must be overriden.

        Args:
            login (str): Login of the user.

        Raises:
            NotImplementedError: Raises to prevent calling this method by super.

        Returns:
            TwichUser: Twich user domain model instance.
        """

        raise NotImplementedError
