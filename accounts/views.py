from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .serializers import UserCreateSerializer, UserLoginSerializer
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework_simplejwt.views import TokenObtainPairView


class RegisterAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class LoginAPIView(TokenObtainPairView):
    serializer_class = UserLoginSerializer
