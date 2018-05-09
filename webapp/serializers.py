from django.contrib.auth.models import User
from rest_framework import serializers

from webapp.models import Photo, Kid


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password")


class KidSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kid
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):
    kids = KidSerializer(read_only=True, many=True)
    """ owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='id'
    )
    """

    class Meta:
        model = Photo
        fields = '__all__'



