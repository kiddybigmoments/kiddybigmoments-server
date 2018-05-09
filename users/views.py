import unicodedata
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status, permissions, generics
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework_jwt.settings import api_settings
from users import serializers
from users.serializers import UsersListSerializer, UserSerializer


class ListUsersView(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.AllowAny,)

    """
    def get(self, request):   Deleted many comment lines. A photo can now be loaded, this has been tested using Postman and the Django Admin Panel. Changed the model, so the migrations must be generated again. 
                              The authentication is disabled for easy testing.
        users = models.CustomUser.objects.all()   # users es un objeto que hay que convertir al formato de salida
        serializer = UsersListSerializer(users, many=True)
        # El serializador obtiene un diccionario por cada usuario de la lista
        return Response(serializer.data)
    """

    """
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Llama a create o a update
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """


class UsersDetailView(APIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request, pk):
        user = get_object_or_404(User, id=pk)   # username=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)
        # Llama al método create de serializers.py
        return Response(serializer.data)

    def put(self, request, pk):
        user = get_object_or_404(User, id=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user, data=request.data)
        # Llama al método update de serializers.py
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    Según REST, put no es lo mismo que patch
    Patch actualiza sólo un campo ---> parámetro "partial" del serializador igual a True
    """
    def delete(self, request, pk):
        user = get_object_or_404(User, id=pk)
        self.check_object_permissions(request, user)
        user.delete()
        #    serializer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        """
            return redirect('home_page')
            redirect_to = request.GET.get("next", "home_page")
            return redirect(redirect_to)
            Tell Angular to notify the error "Usuario incorrecto o inactivo"
            return render(request, "login_form.html", {'form': form})
        """



