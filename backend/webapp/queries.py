import graphene
from pprint import pprint
from webapp import models
from webapp import types
from .query.expense_query import ExpenseQuery
from .mutation.expense_mutation import AddExpense


class Query(ExpenseQuery, graphene.ObjectType):
    pass

# class Mutation(Mutation, graphene.ObjectType):
#     pass


class Mutation(graphene.ObjectType):
    add_expense = AddExpense.Field()
