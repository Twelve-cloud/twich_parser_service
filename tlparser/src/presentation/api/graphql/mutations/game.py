# """
# game_mutations.py: File, containing graphql mutations for twich game.
# """


# import strawberry
# from dependency_injector.wiring import Provide, inject
# from application.dtos.graphql_types.twich.game_type import TwichGameGraphQLType
# from container import Container
# from presentation.controllers.twich.game_controller import TwichGameController


# @inject
# async def parse_game(
#     game_name: str,
#     controller: TwichGameController = Provide[Container.twich_game_w_controller],
# ) -> None:
#     """
#     parse_game: Produce message to kafka to parse games.

#     Args:
#         game_name (str): Name of the game.
#     """

#     await controller.parse_game(game_name)


# @inject
# async def private_parse_game(
#     game_name: str,
#     controller: TwichGameController = Provide[Container.twich_game_w_controller],
# ) -> TwichGameGraphQLType:
#     """
#     private_parse_game: Parse twich game and return result as twich game.

#     Args:
#         game_name (str): Name of the game.
#         controller (TwichGameController): Twich game controller.

#     Returns:
#         TwichGameGraphQLType: Twich game.
#     """

#     return TwichGameGraphQLType(**(await controller.private_parse_game(game_name)).dict())


# @inject
# async def delete_game(
#     game_name: str,
#     controller: TwichGameController = Provide[Container.twich_game_w_controller],
# ) -> None:
#     """
#     delete_game_by_name: Delete twich game.

#      Args:
#         game_name (str): Name of the game.
#         controller (TwichGameController): Twich game controller.
#     """

#     await controller.delete_game_by_name(game_name)


# @strawberry.type
# class TwichGameMutation:
#     """
#     TwichGameMutation: Mutation for twich game.
#     """

#     @strawberry.mutation
#     async def parse_game(self, game_name: str) -> None:
#         """
#         parse_game: Resolver for parsing twich game via kafka.

#         Args:
#             game_name (str): Name of the game.
#         """

#         await parse_game(game_name)

#     @strawberry.mutation
#     async def private_parse_game(self, game_name: str) -> TwichGameGraphQLType:
#         """
#         private_parse_game: Resolver for parsing twich game.

#         Args:
#             game_name (str): Name of the game.
#         """

#         return await private_parse_game(game_name)

#     @strawberry.mutation
#     async def delete_game(self, game_name: str) -> None:
#         """
#         delete_game: Resolver for deleting twich game.

#         Args:
#             game_name (str): Name of the game.
#         """

#         await delete_game(game_name)
