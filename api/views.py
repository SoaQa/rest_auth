from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.serializers import UserSerializer, LoginSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer


class AuthViewSet(viewsets.ViewSet):
    permission_classes = []

    def create(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = authenticate(
                username=request.data['username'],
                password=request.data['password'],
            )
            if user:
                login(request, user)
                serializer = UserSerializer(user)
                return Response(serializer.data)
            else:
                raise AuthenticationFailed()
