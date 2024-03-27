"""
user.py: File, containing twich user query handlers.
"""


from automapper import mapper
from application.dto import TwichUserDTO
from application.interfaces.handler import IQueryHandler
from application.interfaces.repository import ITwichUserRepository
from application.queries import GetAllTwichUsers, GetTwichUserByLogin
from domain.models import TwichUser


class GetTwichUserByLoginHandler(IQueryHandler[GetTwichUserByLogin, TwichUserDTO]):
    def __init__(
        self,
        repository: ITwichUserRepository,
    ) -> None:
        self.repository: ITwichUserRepository = repository

    async def handle(self, query: GetTwichUserByLogin) -> TwichUserDTO:
        user: TwichUser = await self.repository.get_user_by_login(query.login)

        return mapper.to(TwichUserDTO).map(user)


class GetAllTwichUsersHandler(IQueryHandler[GetAllTwichUsers, list[TwichUserDTO]]):
    def __init__(
        self,
        repository: ITwichUserRepository,
    ) -> None:
        self.repository: ITwichUserRepository = repository

    async def handle(self, query: GetAllTwichUsers) -> TwichUserDTO:
        users: list[TwichUser] = await self.repository.all()

        return [mapper.to(TwichUserDTO).map(user) for user in users]
