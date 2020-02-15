from rest_framework import serializers
from apps.core.models import Reseller


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

    # Ensure passwords are at least 8 characters long, no longer than 128
    # characters, and can not be read by the client.
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = Reseller
        fields = ['email', 'password', 'first_name', 'cpf']

    def create(self, validated_data):
        # Use the `create_user` method we wrote earlier to create a new user.

        user = Reseller.objects.create_user(**validated_data)

        return user