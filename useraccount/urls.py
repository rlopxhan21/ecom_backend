from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)
from rest_framework_social_oauth2.views import (
    ConvertTokenView,
    RevokeTokenView
)

from .views import UserDetailView

urlpatterns = [
    path('token-create/', TokenObtainPairView.as_view(), name='token_create'),
    path('token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token-blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),

    path('convert-token/', ConvertTokenView.as_view(), name='convert_token'),
    path('revoke-token/', RevokeTokenView.as_view(), name='revoke_token'),

    path('me/', UserDetailView.as_view(), name="user-detail"),
]