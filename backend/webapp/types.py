import graphene
from graphene_django import DjangoObjectType
from webapp import models


class ExpenseType(DjangoObjectType):
    class Meta:
        model = models.Expense
