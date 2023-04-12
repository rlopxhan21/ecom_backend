from rest_framework import serializers

from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    """This serializer is for providing the user read only user information. """
    class Meta:
        model = CustomUser
        fields = ['full_name', 'email', 'last_login', 'is_staff', 'is_superuser']

class CustomUserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
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
            raise serializers.ValidationError({"error": "Password and Confirm Password must match! "})
        
        account = CustomUser(email=self.validated_data['email'], full_name=self.validated_data['full_name'])
        account.set_password(password)
        account.save()

        return account