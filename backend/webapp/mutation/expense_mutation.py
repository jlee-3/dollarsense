import graphene
from pprint import pprint
from webapp import models, types
from webapp.dto import expense
from datetime import datetime


class AddExpense(graphene.Mutation):
    class Arguments:
        input = expense.AddExpenseInput()

    expense = graphene.Field(types.ExpenseType)

    # @staticmethod
    # @classmethod
    def mutate(root, info, input=None):
        expenseEntity = models.Expense(
            description=input.description,
            amount=input.amount,
            spotRate=input.spotRate,
            currency=input.currency,
            category=input.category,
            subCategory=input.subCategory,
            createdAt=input.createdAt,
            updatedAt=input.updatedAt,
        )

        expenseEntity.save()
        print('addExpense expenseEntity: ')
        pprint(expenseEntity.__dict__)

        return AddExpense(expense=expenseEntity)


class EditExpense(graphene.Mutation):
    class Arguments:
        input = expense.EditExpenseInput()

    expense = graphene.Field(types.ExpenseType)

    def mutate(root, info, input=None):
        id = input.pop('id')
        expenseEntity = models.Expense.objects.get(id=id)
        # expenseEntity = models.Expense.objects.filter(id=id).update(**input)

        for key, value in input.items():
            setattr(expenseEntity, key, value)

        setattr(expenseEntity, 'updatedAt', datetime.now())

        expenseEntity.save()
        print('editExpense expenseEntity: ')
        pprint(expenseEntity.__dict__)

        return EditExpense(expense=expenseEntity)


class DeleteExpense(graphene.Mutation):
    class Arguments:
        input = expense.DeleteExpenseInput()

    # expense = graphene.Field(types.ExpenseType)
    # output = graphene.List(types.ExpenseOutput)
    output = graphene.Field(types.DeleteOutput)

    def mutate(root, info, input=None):
        id = input.id
        ids = input.ids

        if id:
            entities = models.Expense.objects.filter(id=id)
            # print('DeleteExpense entities: ', entities.values())

        elif ids:
            entities = models.Expense.objects.filter(id__in=ids)
            # print('DeleteExpense entities: ', entities.values())

        # expenseEntity = models.Expense.objects.get(id=id)
        # returnEntities = expenseEntity
        # expenseEntity.delete()
        # returnEntity.id = id

        deleteResult = entities.delete()
        result = {
            'isSuccess': False if deleteResult[0] == 0 else True,
            'affectedEntities': deleteResult[0]
        }

        print('DeleteExpense expenseEntity: ', result)
        # pprint(returnEntity.__dict__)

        return DeleteExpense(output=result)
