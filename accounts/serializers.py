from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Account
import re


class AccountSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[
        UniqueValidator(
            queryset=Account.objects.all(),
            message='A user with that email already exists.'
        )]
    )

    username = serializers.CharField(validators=[
        UniqueValidator(
            queryset=Account.objects.all(),
            message='A user with that username already exists.'
        )]
    )

    class Meta:
        model = Account
        fields = ["id", "username", "nickname", "email", "password", "first_name", "last_name", "birthdate", "profile_picture"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict) -> Account:
        regex = r"\s"
        result = re.search(regex, validated_data['username'])

        if result:
            raise SyntaxError("Username value may contain only letters and numbers.")

        return Account.objects.create_user(**validated_data)

    def update(self, instance: Account, validated_data: dict) -> Account:
        for key, value in validated_data.items():
            if key == 'password':
                instance.set_password(validated_data['password'])
            elif key == 'username':
                regex = r"\s"
                result = re.search(regex, validated_data['username'])
                if result:
                    raise SyntaxError("Username value may contain only letters and numbers.")
                else:
                    setattr(instance, key, value)
            else:
                setattr(instance, key, value)

        instance.save()
        
        return instance
