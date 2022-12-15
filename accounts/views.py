from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from .serializers import UserCreateSerializer, UserLoginSerializer
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework_simplejwt.views import TokenObtainPairView

from accounts.models import Profile
from accounts.serializers import ProfileSerializer

class RegisterAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class LoginAPIView(TokenObtainPairView):
    serializer_class = UserLoginSerializer

class ProfileAPIView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = "id"
    lookup_url_kwarg = "profile_id"