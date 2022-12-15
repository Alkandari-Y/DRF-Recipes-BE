from django.urls import path
from accounts.views import ProfileAPIView

urlpatterns = [
    path('profile/<int:profile_id>/', ProfileAPIView.as_view(), name='profile')
]
