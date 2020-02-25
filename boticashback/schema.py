import graphene
import graphql_jwt
from apps.authcb.schema import UserProfileQuery


class Query(
    UserProfileQuery,
    graphene.ObjectType,
):
    pass


# class Mutation(apps.authcb.schema.Mutation):
#     login = graphql_jwt.ObtainJSONWebToken.Field()
#     verify_token = graphql_jwt.Verify.Field()
#     refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query)



