import graphene


class AddExpenseInput(graphene.InputObjectType):
    title = graphene.String(required=True)
    amount = graphene.Float(required=True)
    spotRate = graphene.Float(required=False, default_value=None)
    currency = graphene.String(required=True)
    category = graphene.String(required=True)
    createdAt = graphene.String(required=False, default_value=None)
    updatedAt = graphene.String(required=False, default_value=None)
