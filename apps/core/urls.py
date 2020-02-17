import os
from django.urls import path, include
from django.contrib.auth.views import LoginView
# from rest_framework.routers import DefaultRouter
from boticashback import settings
from apps.core.views import ResellerViewSet, ResellerListView, ReadMeView, ResellerCreateView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from boticashback.urls import router

app_name = 'core'
# router = DefaultRouter()
router.register('revendedores', ResellerViewSet, basename='resellers')

# router.register('api/token/', TokenObtainPairView.as_view(), basename='token_obtain_pair')
# router.register('api/token/refresh/', TokenRefreshView, basename='token_refresh')

# path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
# path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

urlpatterns = [
    # path('api/v1/', include(router.urls)),
    path('', ResellerListView.as_view(), name='home'),
    path('readme/', ReadMeView.as_view(), {'rst_file': os.path.join(settings.BASE_DIR, 'README.rst')}, name='readme'),
    path('reseler/', ResellerCreateView.as_view(), name='reseller'),
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),
    # path('revendedores/', include(router.urls)),
]
