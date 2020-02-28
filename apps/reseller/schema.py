import graphene
#from graphene_django import DjangoObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.rest_framework.mutation import SerializerMutation
from django.contrib.auth import get_user_model
from apps.reseller.models import Reseller
from apps.reseller.serializers import ResellerSerializer
User = get_user_model()


class ResellerType(DjangoObjectType):
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


class CreateReseller(graphene.Mutation):
    class Arguments:
        full_name = graphene.String(required=True)
        cpf = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    reseller = graphene.Field(ResellerType)

    # def mutate(self, info, full_name, cpf, email, password ):
    #     new_reseller = Reseller.objects.create(full_name=full_name, cpf=cpf, email=email, password=password)
    #     new_reseller.save()
    #     return CreateReseller(reseller=new_reseller)

    def mutate(self, info, full_name, cpf, email, password ):
        # new_reseller = Reseller.objects.create()
        new_reseller = Reseller.objects.create()
        new_reseller.full_name=full_name
        new_reseller.cpf=cpf
        new_reseller.email=email
        password=password
        new_reseller.save()
        return CreateReseller(reseller=new_reseller)

