import os
from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from apps.reseller.views import ResellerViewSet, ResellerListView, ReadMeView, ResellerCreateView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from rest_framework import routers
# from boticashback.urls import router
from boticashback.settings import base as settings

app_name = 'reseller'
# router = routers.SimpleRouter()
# router.register('revendedores', ResellerViewSet, basename='resellers')

urlpatterns = [
    # path('api/v1/', include(router.urls)),
    path('', login_required(ResellerListView.as_view()), name='home'),
    path('readme/', ReadMeView.as_view(), {'rst_file': os.path.join(settings.BASE_DIR, 'README.rst')}, name='readme'),
    # path('cadastro/', staff_member_required(ResellerCreateView.as_view()), name='reseller'),
    path('cadastro/', ResellerCreateView.as_view(), name='reseller'),
    path('login/', LoginView.as_view(template_name='reseller/login.html'), name='login'),
]
