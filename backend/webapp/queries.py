import graphene
from pprint import pprint
from webapp import models
from webapp import types
from .query.expense_query import ExpenseQuery


class Query(ExpenseQuery, graphene.ObjectType):
    pass
