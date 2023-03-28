import graphene
from pprint import pprint
from webapp import models
from webapp import types


class ExpenseQuery(graphene.ObjectType):
    # expense = graphene.Field(types.ExpenseType)
    all_expenses = graphene.List(types.ExpenseType)

    def resolve_all_expenses(root, info):
        # for expense in models.Expense.objects.all():
        #     print('[loop] expense.category: ', expense.category)
        #     modifiedExpense = expense
        #     if (expense.category == 'Clothes'):
        #         modifiedExpense.category = 'News'

        #     result = modifiedExpense

        # print('individual model: ', models.Expense.objects.get(pk=1))
        # print('result: ', result)
        # pprint(models.Expense.objects.all())
        result = models.Expense.objects.all()

        return (
            result
        )
