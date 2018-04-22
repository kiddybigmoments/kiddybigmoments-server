from rest_framework import serializers

from webapp.models import Photo, Kid, Parents


class ParentsSerializer(serializers.ModelSerializer):
    # kids = serializers.PrimaryKeyRelatedField(many=True, queryset=Kid.objects.all)
    mother = serializers.ReadOnlyField(source='mother.username')
    father = serializers.ReadOnlyField(source='father.username')

    class Meta:
        model = Parents
        fields = '__all__'


class KidSerializer(serializers.ModelSerializer):
    parents = ParentsSerializer(read_only=True, many=False)

    class Meta:
        model = Kid
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):
    kids = KidSerializer(read_only=True, many=True)

    class Meta:
        model = Photo
        fields = '__all__'


class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)

