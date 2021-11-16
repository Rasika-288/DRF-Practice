from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        exclude = ['password', 'updated_at', 'is_active']
