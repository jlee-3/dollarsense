import graphene
from pprint import pprint
from webapp import models, types
from webapp.dto import expense


class AddExpense(graphene.Mutation):
    class Arguments:
        input = expense.AddExpenseInput()

    expense = graphene.Field(types.ExpenseType)

    # @staticmethod
    # @classmethod
    def mutate(root, info, input=None):
        expenseEntity = models.Expense(
            title=input.title,
            amount=input.amount,
            spotRate=input.spotRate,
            currency=input.currency,
            category=input.category,
            createdAt=input.createdAt,
            updatedAt=input.updatedAt,
        )

        expenseEntity.save()
        print('addExpense expenseEntity: ')
        pprint(expenseEntity.__dict__)

        return AddExpense(expense=expenseEntity)
