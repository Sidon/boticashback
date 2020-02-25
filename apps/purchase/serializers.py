import requests
from rest_framework import serializers
from apps.purchase.models import Purchase, ApprovedCPF
from apps.reseller.serializers import ResellerSerializer


class PurchaseSerializer(serializers.ModelSerializer):
    # reseller = ResellerSerializer(read_only=True)

    class Meta:
        model = Purchase
        fields = ('id', 'date_purchase', 'code', 'purchase_value')
        read_only_fields = ('id',)

    def create(self, validated_data):
        reseller = self.context['request'].user.reseller
        approved_cpfs = ApprovedCPF.objects.all()
        validated_data['status'] = 'APROVADO' if reseller.cpf in approved_cpfs else 'EM_VALIDACAO'
        validated_data['reseller'] = reseller
        purchase = Purchase.objects.create(**validated_data)
        return purchase


class PurchaseAdminSerializer(serializers.ModelSerializer):
    reseller = ResellerSerializer
    class Meta:
        model = Purchase
        fields = ('id', 'reseller', 'date_purchase', 'code', 'purchase_value')
        read_only_fields = ('id',)


class AprovedCPFSerializer(serializers.ModelSerializer):
    # reseller = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    class Meta:
        model = ApprovedCPF
        fields = ('id', 'cpf', 'description')

