from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(help_text="email")
    password = serializers.CharField(help_text="password")

    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
