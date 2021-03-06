import requests
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.generics import (CreateAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView)
from .serializers import AprovedCPFSerializer, PurchaseSerializer, PurchaseAdminSerializer
from .models import ApprovedCPF, Purchase


# Backend
class ApprovedCPFViewSet(GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = AprovedCPFSerializer
    queryset = ApprovedCPF.objects.all()


# Backend
class PurchaseViewSet(GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    permission_classes = (IsAuthenticated,)
    def get_serializer_class(self):
        if self.basename == 'admin-compras':
            return PurchaseAdminSerializer
        return PurchaseSerializer
    queryset = Purchase.objects.all()


# Backend
class CashbackAcumullated(GenericViewSet):
    permission_classes = (IsAuthenticated,)
    def list(self, request):
        url = 'https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/cashback?cpf=12312312323'
        headers = {'token': 'ZXPURQOARHiMc6Y0flhRC1LVlZQVFRnm'}
        results = requests.get(url=url, headers=headers).json()
        return Response(results)
