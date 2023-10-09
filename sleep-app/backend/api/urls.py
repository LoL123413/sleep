# api_app/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TagViewSet, RegistrationAPIView, LoginAPIView, TokenRefreshAPIView, gen_api_key
from django.contrib.auth import get_user_model
User = get_user_model()

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'Tag', TagViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('gen_key/', gen_api_key, name = "GAK"),
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='token_obtain_pair'),
    path('token-refresh/', TokenRefreshAPIView.as_view(), name='token_refresh'),
]
