import os
from django.contrib import admin
from django.urls import include, path
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from graphene_django.views import GraphQLView
from .views import HomePageView
from boticashback.settings import base as settings
from apps.reseller.views import ResellerViewSet, ReadMeView
from apps.purchase.views import ApprovedCPFViewSet, PurchaseViewSet, CashbackAcumullated
from apps.cashback.views import DebitViewSet, RangeViewSet

router = DefaultRouter()
router.register('revendedores', ResellerViewSet, basename='reselers')
router.register('cadastro-cpf-pre-aprovado', ApprovedCPFViewSet, basename='cpfs')
router.register('cadastro-de-compra', PurchaseViewSet, basename='compras')
router.register('cadastro-de-compra-admin', PurchaseViewSet, basename='admin-compras')
router.register('cashback-acumulada', CashbackAcumullated, basename='cashback-acumulado')
router.register('cashback-lista-local', DebitViewSet, basename='cashback-lista')
router.register('cashback-intervalos', RangeViewSet, basename='cashback-intervalos')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.reseller.urls')),
    # path('', ReadMeView.as_view(), {'rst_file': os.path.join(settings.BASE_DIR, 'README.rst')}, name='home'),
    # path('', ReadMeView.as_view(), {'rst_file': os.path.join(settings.BASE_DIR, 'README.rst')}, name='home'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/', include(router.urls)),
    path("graphiql/", GraphQLView.as_view(graphiql=True))
]


try:
    ENV = os.environ['ENVIRONMENT']
except:
    ENV = 'local'

if settings.DEBUG and ENV == 'local':
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

