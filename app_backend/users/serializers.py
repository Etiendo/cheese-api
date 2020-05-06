from rest_framework import serializers
from app_backend.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)
