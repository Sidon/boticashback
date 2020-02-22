from rest_framework import serializers
from apps.purchase.models import Purchase, ApprovedCPF
from apps.reseller.serializers import ResellerSerializer
# from apps.purchase.


class PurchaseSerializer(serializers.ModelSerializer):
    reseller = ResellerSerializer(read_only=True)
    class Meta:
        model = Purchase
        fields = ('id', 'purchase_data', 'reseller', 'codigo', 'value')


class AprovedCPFSerializer(serializers.ModelSerializer):
    # reseller = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    class Meta:
        model = ApprovedCPF
        fields = ('id', 'cpf', 'description')

    # def create(self, validated_data):
    #     print('cpf====>', validated_data)
    #
    #     cpf = ApprovedCPF.objects.create(**validated_data)
    #     return cpf


