import os
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from boticashback import settings
from apps.core.views import ResellerViewSet, ResellerListView, ReadMeView, ResellerCreateView

app_name = 'core'

router = DefaultRouter()
router.register('revendedores', ResellerViewSet, basename='resellers')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', ResellerListView.as_view(), name='home'),
    path('readme/', ReadMeView.as_view(), {'rst_file': os.path.join(settings.BASE_DIR, 'README.rst')}, name='readme'),
    path('reseler/', ResellerCreateView.as_view(), name='reseller'),
    # path('revendedores/', include(router.urls)),
]
