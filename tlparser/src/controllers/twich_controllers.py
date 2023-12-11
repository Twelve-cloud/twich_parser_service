"""
twich_controllers.py: File, containing controllers for a twich app.
"""


from schemas.twich_schemas import TwichGameSchema, TwichUserSchema, TwichStreamSchema


class TwichController:
    """
    TwichController: Class, that represents twich controller. It handles every http exception.
    """

    async def parse_user(self, user_id: str) -> TwichUserSchema:  # type: ignore
        pass

    async def parse_game(self, game_id: str) -> TwichGameSchema:  # type: ignore
        pass

    async def parse_stream(self, user_id: str) -> TwichStreamSchema:  # type: ignore
        pass
