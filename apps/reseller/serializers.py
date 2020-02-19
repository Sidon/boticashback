from rest_framework import serializers
from apps.reseller.models import Reseller


class ResellerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = Reseller
        fields = ('id', 'full_name', 'cpf', 'email', 'password')

    def create(self, validated_data):
        reseller = Reseller.objects.create_reseller(**validated_data)
        return reseller
