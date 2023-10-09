from django.urls import path
from .views import home, SignUp, profile
from .email_sender import CustomPasswordResetView
from django.contrib.auth import get_user_model
User = get_user_model()
urlpatterns = [
]
