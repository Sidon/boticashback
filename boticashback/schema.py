import graphene
import graphql_jwt
from apps.authcb.schema import UserProfileQuery
from apps.purchase.schema import ApprovedCPFQuery


class Query(
    UserProfileQuery,
    ApprovedCPFQuery,
    graphene.ObjectType,
):
    pass


# class Mutation(apps.authcb.schema.Mutation):
#     login = graphql_jwt.ObtainJSONWebToken.Field()
#     verify_token = graphql_jwt.Verify.Field()
#     refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query)



