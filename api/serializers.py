from django.contrib.auth.models import User
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class UserSerializer(LoginSerializer):
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    email = serializers.EmailField()
