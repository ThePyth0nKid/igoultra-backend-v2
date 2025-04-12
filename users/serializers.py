from rest_framework import serializers
from .models import CustomUser  # oder dein User-Modell

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "avatar", "xp", "level"]  # passe ggf. an
