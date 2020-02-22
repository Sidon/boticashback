from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import (CreateAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView)
from .serializers import AprovedCPFSerializer
from .models import ApprovedCPF


# Backend
class ApprovedCPFViewSet(GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    # Allow any user (authenticated or not) to hit this endpoint.
    # permission_classes = (IsAdminUser,)
    permission_classes = (IsAuthenticated,)
    serializer_class = AprovedCPFSerializer
    queryset = ApprovedCPF.objects.all()


class CadastroCPFView(CreateAPIView):
    serializer_class = AprovedCPFSerializer
    queryset = ApprovedCPF.objects.all()
