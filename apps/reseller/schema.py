import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
from apps.reseller.models import Reseller
User = get_user_model()


class ResellerType(DjangoObjectType, token=graphene.String(required=True)):
    class Meta:
        model = Reseller


class ResellerQuery(graphene.ObjectType):
    reseller = graphene.Field(
        ResellerType,
        id=graphene.Int(),
        cpf=graphene.String(required=True),
        full_name=graphene.String(required=True),
    )

    # all_resellers = graphene.List(ResellerType, token=graphene.String(required=True))
    all_resellers = graphene.List(ResellerType, token=graphene.String(required=False))


    def resolve_all_resellers(self, info, **kwargs):
        return Reseller.objects.all()

    def resolve_reseller(self, info, **kwargs):
        id = kwargs.get('id')
        if id:
            return Reseller.objects.get(pk=id)
        return None


