from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)

from .views import UserRegistrationView, UserDetailView, PasswordResetView, PasswordResetConfirmView


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name="register"),
    
    path('token-create/', TokenObtainPairView.as_view(), name='token_create'),
    path('token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token-blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),

    path('password-reset/', PasswordResetView.as_view(), name="password-reset"),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password-reset-confirm"),

    path('me/', UserDetailView.as_view(), name="user-detail"),
]