
from rest_framework import mixins, generics, permissions, serializers

from .models import CustomUser
from .serializers import CustomUserSerializer

class UserDetailView(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id
        return CustomUser.objects.filter(id=user_id)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)