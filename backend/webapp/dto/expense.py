import graphene


class AddExpenseInput(graphene.InputObjectType):
    description = graphene.String(required=True)
    amount = graphene.Float(required=True)
    spotRate = graphene.Float(required=False, default_value=None)
    currency = graphene.String(required=True)
    category = graphene.String(required=True)
    subCategory = graphene.String(required=False, default_value=None)
    createdAt = graphene.String(required=False, default_value=None)
    updatedAt = graphene.String(required=False, default_value=None)


class DeleteExpenseInput(graphene.InputObjectType):
    id = graphene.String(required=False)
    # ids = graphene.String(required=False)
