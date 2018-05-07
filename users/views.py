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
from users import models, serializers
from users.models import CustomUser
from users.serializers import UsersListSerializer, UserSerializer


class ListUsersView(generics.ListCreateAPIView):

    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.AllowAny,)

    """
    def get(self, request):
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

    queryset = models.CustomUser.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [UsersPermission]

    def get(self, request, pk):
        user = get_object_or_404(models.CustomUser, username=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)
        # Llama al método create de serializers.py
        return Response(serializer.data)

    def put(self, request, pk):
        user = get_object_or_404(models.CustomUser, username=pk)
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
        user = get_object_or_404(models.CustomUser, username=pk)
        self.check_object_permissions(request, user)
        user.delete()
        #    serializer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            # return redirect('home_page')
            # redirect_to = request.GET.get("next", "home_page")
            # return redirect(redirect_to)
            # Tell Angular to notify the error "Usuario incorrecto o inactivo"
            # return render(request, "login_form.html", {'form': form})


class RegisterView(generics.CreateAPIView):

    queryset = models.CustomUser.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        # form = SignupForm(request.POST)
        """
        if Angular form data are valid():
            Retrieve Angular form fields and tell Angular to clean its form fields
            username = content of the Angular form username
            raw_password = content of the Angular form password
        """
        username = request.data.get("username", "")   # request.POST.get("username")
        raw_password = request.data.get("email", "")
        print(" ============ The username is: " + username + "  " + raw_password)
        # user.set_password(raw_password)
        # user.save()
        # authenticated_user = authenticate(username=username, password=raw_password)
        # django_login(request, authenticated_user)
        # return Response(authenticated_user)
        serializer = UserSerializer(data=request.data)
        # if serializer.is_valid():
        if not username:
            return Response(
                data={
                    "message": "Debe introducir un nombre de usuario y una contraseña válidos"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
            # Tell Angular to redirect to the Home Page for that user

        # Falta considerar el caso de que el nombre ya exista

        else:
            new_user = CustomUser.objects.create_user(
                username=username, password=raw_password
            )
            serializer.save()
            # new_user.save()
            return Response(
                # data=serializer(new_user).data,
                data={
                    'username': username,
                    'password': raw_password
                },
                status=status.HTTP_201_CREATED
            )

