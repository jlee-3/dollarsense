import graphene
from pprint import pprint
from webapp import models
from webapp import types
from webapp.dto import expense
from datetime import date


class ExpenseQuery(graphene.ObjectType):
    # expense = graphene.Field(types.ExpenseType)
    # all_expenses = graphene.List(types.ExpenseType)

    expenses = graphene.List(
        types.ExpenseType,
        input=expense.ExpenseQueryInput())

    def resolve_expenses(root, info, input):
        fields = list(input.keys())

        def listIntersection(listA, listB):
            return [el for el in listA if el in listB]

        orderBy = None
        if 'orderBy' in input:
            orderBy = input.orderBy
            fields.remove('orderBy')

        # Firstly filter for time range or unit
        # gte & lte is inclusive of range endpoints
        if len(input) > 1 and 'startDate' in fields and 'endDate' in fields:
            result = models.Expense.objects.filter(createdAt__gte=input.startDate,
                                                   createdAt__lte=input.endDate)
        elif listIntersection(fields, ['date', 'month', 'year']):
            timeUnit = listIntersection(fields, ['date', 'month', 'year'])[0]
            # dynamically construct filter argument
            timeArgs = {'{0}__{1}'.format(
                'createdAt', timeUnit): input[timeUnit], }
            result = models.Expense.objects.filter(**timeArgs)
        else:
            result = models.Expense.objects.all()

        # Next, chain any additional filters
        if listIntersection(fields, ['currency', 'category', 'subCategory']):
            stackedArgs = {}
            for field in fields:
                if field in ['currency', 'category', 'subCategory']:
                    print('[stacked] field: ', field)
                    stackedArgs[field] = input[field]

            result = result.filter(**stackedArgs)

        if orderBy:
            result = result.order_by(orderBy)

        return result

    # def resolve_all_expenses(root, info, input=None):
    #     print('input: ', input)
    #     # for expense in models.Expense.objects.all():
    #     #     print('[loop] expense.category: ', expense.category)
    #     #     modifiedExpense = expense
    #     #     if (expense.category == 'Clothes'):
    #     #         modifiedExpense.category = 'News'

    #     #     result = modifiedExpense

    #     # print('individual model: ', models.Expense.objects.get(pk=1))
    #     # print('result: ', result)
    #     # pprint(models.Expense.objects.all())
    #     # result = models.Expense.objects.all()
    #     result = DjangoFilterConnectionField(types.ExpenseType)
    #     print('result: ', result)
    #     return (
    #         result
    #     )
