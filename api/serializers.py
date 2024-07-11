from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
