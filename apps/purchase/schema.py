import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
from apps.purchase.models import Purchase, ApprovedCPF
User = get_user_model()


class ApprovedCPFType(DjangoObjectType, token=graphene.String(required=True)):
    class Meta:
        model = ApprovedCPF


class ApprovedCPFQuery(graphene.ObjectType):
    approved_cpf = graphene.Field(
        ApprovedCPFType,
        id=graphene.Int(),
        cpf=graphene.String(required=True),
        reseller=graphene.String(required=True),
        description=graphene.String(),
    )

    all_cpfs = graphene.List(ApprovedCPFType, token=graphene.String(required=True))


    def resolve_all_cpfs(self, info, **kwargs):
        return ApprovedCPF.objects.all()

    def resolve_approved_cpf(self, info, **kwargs):
        id = kwargs.get('id')
        if id:
            return ApprovedCPF.objects.get(pk=id)
        return None




class PurchaseType(DjangoObjectType, token=graphene.String(required=True)):
    class Meta:
        model = Purchase



class PurchaseQuery(graphene.ObjectType):
    purchase = graphene.Field(
        PurchaseType,
        purchase_value=graphene.String(required=True),
        reseller=graphene.String(required=True),
        code=graphene.String(),
        date_purchase=graphene.String(),
        cashback_credit_value=graphene.String(),
        status=graphene.String(),
        created_at=graphene.String(),
        update_at=graphene.String(),
    )

    # all_purchase = graphene.List(PurchaseType, token=graphene.String(required=True))
    all_purchase = graphene.List(PurchaseType, token=graphene.String(required=False))



    def resolve_all_purchase(self, info, **kwargs):
        return Purchase.objects.all()

    def resolve_purchase(self, info, **kwargs):
        id = kwargs.get('id')
        if id:
            return Purchase.objects.get(pk=id)

        return None












# class Mutation(graphene.ObjectType):
#     create_user = CreateUser.Field()