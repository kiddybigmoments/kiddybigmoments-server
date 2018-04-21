from rest_framework import serializers
from .models import Photo, Kid


class KidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kid
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)

