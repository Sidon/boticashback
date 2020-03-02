import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
from apps.cashback.models import CashbackRange, CashbackDebit,CashbackPayment

User = get_user_model()


class CashbackRangeType(DjangoObjectType, token=graphene.String(required=True)):
    class Meta:
        model = CashbackRange


class CashbackRangeQuery(graphene.ObjectType):
    cashback_range = graphene.Field(
        CashbackRangeType,
        id=graphene.Int(),
        cpf=graphene.String(required=True),
        full_name=graphene.String(required=True),
    )

    # all_cashback_range = graphene.List(CashbackRangeType, token=graphene.String(required=True))
    all_cashback_range = graphene.List(CashbackRangeType, token=graphene.String(required=False))

    def resolve_all_cashback_range(self, info, **kwargs):
        return CashbackRange.objects.all()

    def resolve_cashback_range(self, info, **kwargs):
        id = kwargs.get('id')
        if id:
            return CashbackRange.objects.get(pk=id)
        return None




class CashbackDebitType(DjangoObjectType, token=graphene.String(required=True)):
    class Meta:
        model = CashbackDebit


class CashbackDebitQuery(graphene.ObjectType):
    cashback_debit = graphene.Field(
        CashbackDebitType,
        id=graphene.Int(),
        cpf=graphene.String(required=True),
        full_name=graphene.String(required=True),
    )

    # all_cashback_debit = graphene.List(CashbackDebitType, token=graphene.String(required=True))
    all_cashback_debit = graphene.List(CashbackDebitType, token=graphene.String(required=False))


    def resolve_all_cashback_debit(self, info, **kwargs):
        return CashbackDebit.objects.all()

    def resolve_cashback_debit(self, info, **kwargs):
        id = kwargs.get('id')
        if id:
            return CashbackDebit.objects.get(pk=id)
        return None



class CashbackPaymentType(DjangoObjectType, token=graphene.String(required=True)):
    class Meta:
        model = CashbackPayment


class CashbackPaymentQuery(graphene.ObjectType):
    cashback_payment = graphene.Field(
        CashbackPaymentType,
        id=graphene.Int(),
        cpf=graphene.String(required=True),
        full_name=graphene.String(required=True),
    )

    # all_cashback_payment = graphene.List(CashbackPaymentType, token=graphene.String(required=True))
    all_cashback_payment = graphene.List(CashbackPaymentType, token=graphene.String(required=False))


    def resolve_all_cashback_payment(self, info, **kwargs):
        return CashbackPayment.objects.all()

    def resolve_cashback_payment(self, info, **kwargs):
        id = kwargs.get('id')
        if id:
            return CashbackPayment.objects.get(pk=id)
        return None
