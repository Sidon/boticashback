"""boticashback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from .views import HomePageView
from boticashback.settings import base as settings
from apps.reseller.views import ResellerViewSet
from apps.purchase.views import ApprovedCPFViewSet, PurchaseViewSet, CashbackAcumullated
from graphene_django.views import GraphQLView

router = DefaultRouter()
router.register('revendedores', ResellerViewSet, basename='reselers')
router.register('cadastro-cpf-pre-aprovados', ApprovedCPFViewSet, basename='cpfs')
router.register('cadastro-de-compra', PurchaseViewSet, basename='compras')
router.register('cadastro-de-compra-admin', PurchaseViewSet, basename='admin-compras')
router.register('cashback-acumulada', CashbackAcumullated, basename='cashback-acumulado')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('revendedores/', include('apps.reseller.urls')),
    path('', HomePageView.as_view(), name='home'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/', include(router.urls)),
    path("graphql", GraphQLView.as_view(graphiql=True)),
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

