# """
# game_queries.py: File, containing graphql queries for twich game.
# """


# import strawberry
# from dependency_injector.wiring import Provide, inject
# from application.dtos.graphql_types.twich.game_type import TwichGameGraphQLType
# from container import Container
# from presentation.controllers.twich.game_controller import TwichGameController


# @inject
# async def get_all_games(
#     controller: TwichGameController = Provide[Container.twich_game_r_controller],
# ) -> list[TwichGameGraphQLType]:
#     """
#     get_all_games: Function, that called by resolver to get all games.

#     Args:
#         controller (TwichGameController): Twich game controller.

#     Returns:
#         list[TwichGameGraphQLType]: List of Twich games.
#     """

#     return [TwichGameGraphQLType(**game.dict()) for game in await controller.get_all_games()]


# @inject
# async def get_game_by_name(
#     game_name: str,
#     controller: TwichGameController = Provide[Container.twich_game_r_controller],
# ) -> TwichGameGraphQLType:
#     """
#     get_game_by_name: Function, that called by resolver to get twich game by name.

#     Args:
#         game_name (str): Name of the twich game.
#         controller (TwichGameController): Twich game controller.

#     Returns:
#         TwichGameGraphQLType: Twich game.
#     """

#     return TwichGameGraphQLType(**(await controller.get_game_by_name(game_name)).dict())


# @strawberry.type
# class TwichGameQuery:
#     """
#     TwichGameQuery: Query for twich game.
#     """

#     @strawberry.field
#     async def twich_games(self) -> list[TwichGameGraphQLType]:
#         """
#         twich_game: Resolver for getting all twich games.

#         Returns:
#             list[TwichGameGraphQLType]: List of Twich games.
#         """

#         return await get_all_games()

#     @strawberry.field
#     async def twich_game(self, game_name: str) -> TwichGameGraphQLType:
#         """
#         twich_game: Resolver for getting game by name.

#         Args:
#             game_name (str): Name of the game.

#         Returns:
#             TwichGameGraphQLType: Twich game.
#         """

#         return await get_game_by_name(game_name)
