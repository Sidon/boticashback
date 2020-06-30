import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
from apps.purchase.models import Purchase, ApprovedCPF
from graphql_jwt.decorators import login_required
User = get_user_model()


# class ApprovedCPFType(DjangoObjectType, token=graphene.String(required=True)):
class ApprovedCPFType(DjangoObjectType):
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
        purchase_value=graphene.Decimal(required=True),
        reseller=graphene.String(required=True),
        code=graphene.String(),
        date_purchase=graphene.Date(),
        cashback_credit_value=graphene.Decimal(),
        status=graphene.String(),
        created_at=graphene.Date(),
        update_at=graphene.Date(),

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


class CreatePurchase(graphene.Mutation):
    class Arguments:
        purchase_value = graphene.Decimal(required=True)
        reseller_id = graphene.String(required=True)
        code = graphene.String(required=True)
        date_purchase = graphene.Date(required=True)

    purchase = graphene.Field(PurchaseType, token=graphene.String(required=False))

    # @login_required
    def mutate(self, info, purchase_value, reseller_id, code, date_purchase):
        new_purchase = Purchase.objects.create(
            purchase_value=purchase_value,
            reseller_id=reseller_id,
            code=code,
            date_purchase=date_purchase,
        )
        return CreatePurchase(purchase=new_purchase)


class CreateAprovedCPF(graphene.Mutation):
    class Arguments:
        cpf=graphene.String(required=True)
        description=graphene.String(required=True)

    cpf = graphene.Field(ApprovedCPFType, token=graphene.String(required=True))
    # cpf = graphene.Field(ApprovedCPFType)

    @login_required
    def mutate(self, info, cpf, description):
        new_cpf = ApprovedCPF.objects.create()
        new_cpf.cpf = cpf
        new_cpf.description = description
        new_cpf.save()
        return CreateAprovedCPF(cpf=new_cpf)

