from rest_framework.authtoken.serializers import serializers

from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "password"]


class UserSerializer(serializers.ModelSerializer):

     password = serializers.CharField(write_only=True) 

     class Meta:
         model = User
         fields = ["id", "email", "username", "role", "password"]

     def create(self, validated_data):
         password = validated_data.pop('password')
         user = User.objects.create(**validated_data)
         user.set_password(password)
         user.save()
         return user
     
     def update(self, instance, validated_data):
         password = validated_data.pop('password', None)
         for key, value in validated_data.items():
             setattr(instance, key, value)
         if password is not None:
             instance.set_password(password)
         instance.save()
         return instance
