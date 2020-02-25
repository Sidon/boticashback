import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
User = get_user_model()


class UserProfileType(DjangoObjectType, token=graphene.String(required=True)):
    class Meta:
        model = User


class UserProfileQuery(graphene.ObjectType):
    user_profile = graphene.Field(
        UserProfileType,
        id=graphene.Int(),
        email=graphene.String(),
        token=graphene.String(required=True)
    )

    all_users = graphene.List(UserProfileType, token=graphene.String(required=True))


    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_user_profile(self, info, **kwargs):
        id = kwargs.get('id')
        nome_completo = kwargs.get('nome_completo')
        if id:
            return User.objects.get(pk=id)

        if nome_completo:
            return User.objects.get(nome=nome_completo)

        return None


# class Mutation(graphene.ObjectType):
#     create_user = CreateUser.Field()
