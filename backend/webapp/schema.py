import graphene
from webapp import queries

schema = graphene.Schema(query=queries.Query, mutation=queries.Mutation)
