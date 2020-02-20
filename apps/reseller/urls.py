import os
from django.urls import path, include
from django.contrib.auth.views import LoginView
from boticashback import settings
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
    path('', ResellerListView.as_view(), name='home'),
    path('readme/', ReadMeView.as_view(), {'rst_file': os.path.join(settings.BASE_DIR, 'README.rst')}, name='readme'),
    path('reseller/', ResellerCreateView.as_view(), name='reseller'),
    path('login/', LoginView.as_view(template_name='reseller/login.html'), name='login'),
]

# urlpatterns += router.urls