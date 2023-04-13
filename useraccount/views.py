from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from decouple import config
from rest_framework import mixins, generics, permissions, status
from rest_framework.response import Response

from .models import CustomUser
from .serializers import CustomUserSerializer, CustomUserRegisterSerializer, UserActivationSerializer, PasswordResetSerializer, PasswordResetConfirmSerializer

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


class UserActivationView(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = UserActivationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = CustomUser.objects.get(email=serializer.validated_data['email'])

        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        activation_url = f"http://localhost:8000/auth/account-activate/{uid}/{token}/"

        send_mail(
            subject= "Account Activation",
            message = f"Click on this link to activate your account: {activation_url}",
            from_email=config("EMAIL_HOST_USER"),
            recipient_list=[user.email],
            fail_silently=False
        )
                
        return Response({'message': "Account Activation link sent successfully!"}, status=status.HTTP_200_OK)


class UserActivationConfirmView(generics.GenericAPIView):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return Response({'message': "Your account is activated successfully!"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Your token is invalid!"}, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetView(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = PasswordResetSerializer

    def post(self, request, *args, **kwargs):
        """Send an email to the user with interactions for resetting their password."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = CustomUser.objects.get(email=serializer.validated_data['email'])

        # Generate a token for the user and send an email with link to reset the password
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        reset_url =  f"http://localhost:8000/auth/password-reset/{uid}/{token}/"

        send_mail(
            subject= "Password Reset",
            message = f"Click on this link to reset your password: {reset_url}",
            from_email=config("EMAIL_HOST_USER"),
            recipient_list=[user.email],
            fail_silently=False
        )

        return Response({'message': "Password reset link sent successfully!"}, status=status.HTTP_200_OK)
    

class PasswordResetConfirmView(mixins.UpdateModelMixin, generics.GenericAPIView):
    serializer_class = PasswordResetConfirmSerializer

    def put(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(pk=uid)

        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            password = make_password(serializer.validated_data['password'])
            user.password = password
            user.save()

            return Response({"message": "Your password's changed sucessfully!"}, status=status.HTTP_201_CREATED)
        
        return Response({'message': 'Your token is invalid!'}, status=status.HTTP_400_BAD_REQUEST)
