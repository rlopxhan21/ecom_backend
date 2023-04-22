from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenBlacklistView
)

from .views import MyTokenObtainPairView, UserRegistrationView, UserDetailView, UserActivationView, UserActivationConfirmView, PasswordResetView, PasswordResetConfirmView, EmailChangeView, EmailChangeConfirmView, PasswordChangeView


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name="register"),


    path('account-activate/', UserActivationView.as_view(), name="account_activate"),
    path('account-activate/<uidb64>/<token>/',
         UserActivationConfirmView.as_view(), name="account_activate_confirm"),

    path('token-create/', MyTokenObtainPairView.as_view(), name='token_create'),
    path('token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token-blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),

    path('password-reset/', PasswordResetView.as_view(), name="password_reset"),
    path('password-reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name="password_reset_confirm"),

    path('email-change/', EmailChangeView.as_view(), name="email_change"),
    path('email-change/<uidb64>/<token>/<eid>/',
         EmailChangeConfirmView.as_view(), name="email_change_confirm"),

    path('password-change/', PasswordChangeView.as_view(), name="password_change"),

    path('me/', UserDetailView.as_view(), name="user_detail"),
]
