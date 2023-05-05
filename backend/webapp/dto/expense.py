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


class EditExpenseInput(graphene.InputObjectType):
    id = graphene.String(required=True)
    description = graphene.String(required=False)
    amount = graphene.Float(required=False)
    spotRate = graphene.Float(required=False)
    currency = graphene.String(required=False)
    category = graphene.String(required=False)
    subCategory = graphene.String(required=False)
    createdAt = graphene.String(required=False)


class DeleteExpenseInput(graphene.InputObjectType):
    id = graphene.String(required=False)
    ids = graphene.List(graphene.String, required=False)
