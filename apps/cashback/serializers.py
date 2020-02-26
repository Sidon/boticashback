from rest_framework import serializers
from apps.cashback.models import CashbackRange, CashbackDebit, CashbackPayment
from apps.purchase.serializers import PurchaseSerializer


class CashbackRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashbackRange
        fields = {'id', 'start_value', 'end_value', 'percentage'}


class CashbackDebitSerializer(serializers.ModelSerializer):
    purchase = PurchaseSerializer(read_only=True)
    class Meta:
        model = CashbackDebit
        fields = ('purchase', 'percentage', 'cashback_value', 'status',)


class CashbackPaymentSerializer(serializers.ModelSerializer):
    cashback_debit = CashbackDebitSerializer(read_only=True)
    purchase = PurchaseSerializer(read_only=True)
    class Meta:
        model = CashbackPayment
        fields = {'cashback_debit', 'purchase', 'date_payment'}
