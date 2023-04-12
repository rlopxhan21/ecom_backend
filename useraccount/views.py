
from rest_framework import mixins, generics, permissions, serializers

from .models import CustomUser
from .serializers import CustomUserSerializer, CustomUserRegisterSerializer

class UserDetailView(mixins.ListModelMixin, generics.GenericAPIView):
    """This view shows the user information of authenticated user."""
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id
        return CustomUser.objects.filter(id=user_id)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

class UserRegistrationView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserRegisterSerializer
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
