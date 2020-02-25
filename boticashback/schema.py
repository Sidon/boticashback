import graphene
import graphql_jwt
from apps.authcb.schema import UserProfileQuery
from apps.purchase.schema import ApprovedCPFQuery, PurchaseQuery
from apps.reseller.schema import ResellerQuery
from apps.cashback.schema import CashbackRangeQuery
from apps.cashback.schema import CashbackDebitQuery
from apps.cashback.schema import CashbackPaymentQuery


class Query(
    UserProfileQuery,
    ApprovedCPFQuery,
    PurchaseQuery,
    ResellerQuery,
    CashbackRangeQuery,
    CashbackDebitQuery,
    CashbackPaymentQuery,
    graphene.ObjectType,

):
    pass


# class Mutation(apps.authcb.schema.Mutation):
#     login = graphql_jwt.ObtainJSONWebToken.Field()
#     verify_token = graphql_jwt.Verify.Field()
#     refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query)



