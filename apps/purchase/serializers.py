from rest_framework import serializers
from apps.purchase.models import Purchase, ApprovedCPF
from apps.reseller.serializers import ResellerSerializer
# from apps.purchase.


class PurchaseSerializer(serializers.ModelSerializer):
    reseller = ResellerSerializer(read_only=True)
    class Meta:
        model = Purchase
        fields = {'id', 'data_purchase', 'reseller', 'codigo', 'value'}


class ApprovedCPFSerializer(serializers.ModelSerializer):
    reseller = ResellerSerializer(read_only=True)

    class Meta:
        model = ApprovedCPF
        fields = {'id', 'reseller'}
