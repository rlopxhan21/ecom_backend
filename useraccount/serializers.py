from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import CustomUser


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['is_staff'] = user.is_staff
        token['is_superuser'] = user.is_superuser

        return token


class CustomUserSerializer(serializers.ModelSerializer):
    """This serializer is for providing the user read only user information. """
    class Meta:
        model = CustomUser
        fields = ['full_name', 'email',
                  'last_login', 'is_staff', 'is_superuser']


class CustomUserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['full_name', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {
                'write_only': True,
                "style": {
                    'input_type': 'password'
                }
            }
        }

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {"message": "Password and Confirm Password must match! "})

        account = CustomUser(
            email=self.validated_data['email'], full_name=self.validated_data['full_name'])
        account.set_password(password)
        account.save()

        return account


class UserActivationSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, email):
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError(
                {"message": "This Email Address is not found in the system!"})

        if user.is_active:
            raise serializers.ValidationError(
                {'message': "This account is already been activated!"})

        return email


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, email):
        try:
            CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError(
                {"message": "This Email Address is not found in the system!"})

        return email


class PasswordResetConfirmSerializer(serializers.Serializer):
    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {"message": "Password and Confirm Password must match! "})

        return password


class EmailChangeSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, email):
        try:
            CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return email

        raise serializers.ValidationError(
            {"message": "This Email Address already exist!"})


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    password1 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    def validate(self, data):
        old_password = data.get("old_password")
        password1 = data.get('password1')
        password2 = data.get('password2')

        if password1 and password2 and password1 != password2:
            raise serializers.ValidationError(
                {"message": "Your new password and new confirm password does not match!"})

        if old_password == password1:
            raise serializers.ValidationError(
                {"message": "Your new password can't be same as old password"})

        return data
