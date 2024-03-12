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
    def __init__(
        self,
        repository: ITwichUserRepository,
    ) -> None:
        self.repository: ITwichUserRepository = repository

    async def handle(self, query: GetTwichUserByLogin) -> dto.TwichUser:
        user: TwichUser = await self.repository.get_user_by_login(query.login)

        return mapper.to(dto.TwichUser).map(user)


class GetAllTwichUsersHandler(IQueryHandler[GetAllTwichUsers, dto.TwichUsers]):
    def __init__(
        self,
        repository: ITwichUserRepository,
    ) -> None:
        self.repository: ITwichUserRepository = repository

    async def handle(self, query: GetAllTwichUsers) -> dto.TwichUsers:
        users: list[TwichUser] = await self.repository.all()

        return dto.TwichUsers(data=[mapper.to(dto.TwichUser).map(user) for user in users])
