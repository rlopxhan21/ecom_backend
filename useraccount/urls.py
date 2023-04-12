from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)

from .views import UserRegistrationView, UserDetailView


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name="register"),
    
    path('token-create/', TokenObtainPairView.as_view(), name='token_create'),
    path('token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token-blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),

    path('me/', UserDetailView.as_view(), name="user-detail"),

]