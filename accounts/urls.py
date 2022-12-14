from django.urls import path
from .views import RegisterAPIView, LoginAPIView

urlpatterns = [
    path("rest/register/", RegisterAPIView.as_view(), name="register"),
    path("rest/login/", LoginAPIView.as_view(), name="login"),
]
