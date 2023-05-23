from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    email = serializers.EmailField()
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=127, write_only=True)

    profile_picture = serializers.CharField(max_length=300, allow_null=True, default=None)
    birthdate = serializers.DateField(allow_null=True, default=None)

    def create(self, validated_data: dict) -> Account:
        return Account.objects.create_user(**validated_data)