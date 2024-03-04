"""
schema.py: File, containing graphql Schema.
"""


import strawberry
from strawberry import Schema
from presentation.api.graphql.mutations.twich.game_mutations import TwichGameMutation
from presentation.api.graphql.queries.twich.game_queries import TwichGameQuery


@strawberry.type
class Query(TwichGameQuery):
    """
    Query: GraphQL query.
    """

    pass


@strawberry.type
class Mutation(TwichGameMutation):
    """
    Mutation: GraphQL mutation.
    """

    pass


schema: Schema = Schema(query=Query, mutation=Mutation)
