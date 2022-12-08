from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.serializers import (
    CharField,
    ModelSerializer,
    EmailField,
)

from accounts.services import create_new_user

User = get_user_model()


class UserLoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        if user.is_staff:
            token["admin"] = True
        return token


class UserCreateSerializer(ModelSerializer):
    username = CharField(write_only=True)
    email = EmailField(write_only=True)
    password = CharField(write_only=True)
    access = CharField(read_only=True)
    refresh = CharField(read_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "access", "refresh"]

    def create(self, validated_data):
        token = UserLoginSerializer.get_token(create_new_user(validated_data))
        validated_data["access"] = str(token.access_token)
        validated_data["refresh"] = str(token)

        return validated_data
