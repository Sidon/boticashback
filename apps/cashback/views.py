from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (CreateAPIView, ListAPIView,)
from apps.cashback.models import CashbackPayment, CashbackDebit, CashbackRange
from apps.cashback.serializers import (CashbackDebitSerializer, CashbackPaymentSerializer, CashbackRangeSerializer,)
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from .serializers import CashbackDebitSerializer


class CreateCashbackRangeView(CreateAPIView):
    serializer_class = CashbackRangeSerializer
    queryset = CashbackRange.objects.all()


# Backend
class DebitViewSet(GenericViewSet, mixins.ListModelMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = CashbackDebitSerializer
    queryset = CashbackDebit.objects.all()


class RangeViewSet(GenericViewSet, mixins.ListModelMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = CashbackRangeSerializer
    queryset = CashbackRange.objects.all()


class CreateCashbackPaymentView(CreateAPIView):
    serializer_class = CashbackPaymentSerializer
    queryset = CashbackPayment.objects.all()


class CreateCashbackDebitView(CreateAPIView):
    serializer_class = CashbackDebitSerializer
    queryset = CashbackDebit.objects.all()
