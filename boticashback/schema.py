import graphene
import graphql_jwt
from apps.purchase.schema import ApprovedCPFQuery, PurchaseQuery
from apps.reseller.schema import ResellerQuery
from apps.cashback.schema import (CashbackRangeQuery, CashbackDebitQuery, CashbackPaymentQuery,)
from apps.reseller.schema import CreateReseller
from apps.purchase.schema import CreatePurchase


class Query(
    ApprovedCPFQuery,
    PurchaseQuery,
    ResellerQuery,
    CashbackRangeQuery,
    CashbackDebitQuery,
    CashbackPaymentQuery,
    graphene.ObjectType,

):
    pass


class Mutation(graphene.ObjectType):
    login = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    create_reseller = CreateReseller.Field()
    create_purchase = CreatePurchase.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)



