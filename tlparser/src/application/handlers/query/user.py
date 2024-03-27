"""
user.py: File, containing twich user query handlers.
"""


from dataclasses import asdict
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

        return TwichUserDTO(**asdict(user, dict_factory=TwichUser.as_dict))


class GetAllTwichUsersHandler(IQueryHandler[GetAllTwichUsers, list[TwichUserDTO]]):
    def __init__(
        self,
        repository: ITwichUserRepository,
    ) -> None:
        self.repository: ITwichUserRepository = repository

    async def handle(self, query: GetAllTwichUsers) -> TwichUserDTO:
        users: list[TwichUser] = await self.repository.all()

        return [TwichUserDTO(**asdict(user, dict_factory=TwichUser.as_dict)) for user in users]
