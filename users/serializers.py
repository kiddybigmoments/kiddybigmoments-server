from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.urls import reverse


class UsersListSerializer(serializers.Serializer):
    # Actúa como un traductor de objetos a tipos primitivos (lo contrario a lo que hace un formulario)
    id = serializers.ReadOnlyField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "username")

    def validate_username(self, data):
        pass
        """
        if self.instance is None and User.objects.filter(username=data).exists():
            # La primera condición se cumple cuando se está creando un usuario
            raise ValidationError("El usuario ya existe")
        if self.instance and self.instance.username == data and User.objects.filter(username=data).exists():
            raise ValidationError("Este nombre de usuario ya existe")
        return data
        """

    def create(self, validated_data):  # Construye un objeto User
        instance = User()
        return self.update(instance, validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username")
        instance.set_password(validated_data.get("password"))
        # El método "set_password" cifra la contraseña
        instance.save()
        return instance
