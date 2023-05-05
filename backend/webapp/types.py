import graphene
from graphene_django import DjangoObjectType
from webapp import models


class ExpenseType(DjangoObjectType):
    class Meta:
        model = models.Expense


class ExpenseOutput(graphene.ObjectType):
    id = graphene.String()
    description = graphene.String()
    amount = graphene.Float()
    spotRate = graphene.Float()
    currency = graphene.String()
    category = graphene.String()
    subCategory = graphene.String()
    createdAt = graphene.Date()
    updatedAt = graphene.Date()


class DeleteOutput(graphene.ObjectType):
    isSuccess = graphene.Boolean()
    affectedEntities = graphene.Int()
