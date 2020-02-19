import os
from django.urls import path, include
from boticashback import settings
from apps.cashback.views import (CreateCashbackDebitView, CreateCashbackPaymentView, CreateCashbackRangeView)
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from boticashback.urls import router


app_name = 'cashback'
router.register('cashback-intervalos', CreateCashbackRangeView, basename='intervalo')
router.register('cashback-resgate', CreateCashbackRangeView, basename='resgate')


# urlpatterns = [
#     # path('revendedores/', include(router.urls)),
# ]
