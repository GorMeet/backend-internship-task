from rest_framework.authtoken.serializers import serializers

from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "password"]


class UserSerializer(serializers.ModelSerializer):
     class Meta:
         model = User
         fields = ["id", "email", "username", "is_manager", "is_admin"]
