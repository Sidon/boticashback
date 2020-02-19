from rest_framework import filters
from rest_framework.generics import (CreateAPIView, ListAPIView,)
from apps.cashback.models import CashbackPayment, CashbackDebit, CashbackRange
from apps.cashback.serializers import (CashbackDebitSerializer, CashbackPaymentSerializer, CashbackRangeSerializer,)


class CreateCashbackRangeView(CreateAPIView):
    serializer_class = CashbackRangeSerializer
    queryset = CashbackRange.objects.all()


class CreateCashbackPaymentView(CreateAPIView):
    serializer_class = CashbackPaymentSerializer
    queryset = CashbackPayment.objects.all()


class CreateCashbackDebitView(CreateAPIView):
    serializer_class = CashbackDebitSerializer
    queryset = CashbackDebit.objects.all()
