"""
user.py: File, containing twich user query handlers.
"""


from automapper import mapper
from application import dto
from application.interfaces.handlers import IQueryHandler
from application.interfaces.repositories import ITwichUserRepository
from application.queries import GetAllTwichUsers, GetTwichUserByLogin
from domain.models import TwichUser


class GetTwichUserByLoginHandler(IQueryHandler[GetTwichUserByLogin, dto.TwichUser]):
    """
    GetTwichUserByLoginHandler: Class, representing get twich user by login query handler.
    This class is interface implementation.

    Bases:
        1) IQueryHandler[GetTwichUserByLogin, dto.TwichUser]: Query handler interface.
           Every query handler should implement this class.
    """

    def __init__(
        self,
        repository: ITwichUserRepository,
    ) -> None:
        """
        __init__: Makes initialization.

        Args:
            repository (ITwichUserRepository): Twich user repository.
        """

        self.repository: ITwichUserRepository = repository

    async def handle(self, query: GetTwichUserByLogin) -> dto.TwichUser:
        """
        handle: Should handler get twich user by login query.
        Must be overriden.

        Args:
            query (GetTwichUserByLogin): Query.

        Returns:
            dto.TwichUser: Twich user.
        """

        user: TwichUser = await self.repository.get_user_by_login(query.login)

        return mapper.to(dto.TwichUser).map(user)


class GetAllTwichUsersHandler(IQueryHandler[GetAllTwichUsers, dto.TwichUsers]):
    """
    GetAllTwichUsersHandler: Class, representing get all twich users query handler.
    This class is interface implementation.

    Bases:
        1) IQueryHandler[GetAllTwichUsers, dto.TwichUsers]: Query handler interface.
           Every query handler should implement this class.
    """

    def __init__(
        self,
        repository: ITwichUserRepository,
    ) -> None:
        """
        __init__: Makes initialization.

        Args:
            repository (ITwichUserRepository): Twich user repository.
        """

        self.repository: ITwichUserRepository = repository

    async def handle(self, query: GetAllTwichUsers) -> dto.TwichUsers:
        """
        handle: Should handle get all twich users query.
        Must be overriden.

        Args:
            query (GetAllTwichUsers): Query.

        Returns:
            dto.TwichUsers: Twich users.
        """

        users: list[TwichUser] = await self.repository.all()

        return dto.TwichUsers(data=[mapper.to(dto.TwichUser).map(user) for user in users])
