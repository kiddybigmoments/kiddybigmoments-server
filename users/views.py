import unicodedata
from django.contrib import messages
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.forms import SignupForm
from users.serializers import UsersListSerializer, UserSerializer


class UsersListAPI(APIView):

    # permission_classes = [UsersPermission]

    def get(self, request):
        users = User.objects.all()   # users es un objeto que hay que convertir al formato de salida
        serializer = UsersListSerializer(users, many=True)
        # El serializador obtiene un diccionario por cada usuario de la lista
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Llama a create o a update
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPI(APIView):

    # permission_classes = [UsersPermission]

    def get(self, request, pk):
        user = get_object_or_404(User, username=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)
        # Llama al método create de serializers.py
        return Response(serializer.data)

    def put(self, request, pk):
        user = get_object_or_404(User, username=pk)
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
        user = get_object_or_404(User, username=pk)
        self.check_object_permissions(request, user)
        user.delete()
        #    serializer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LoginView(APIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        content = {
            'user': unicodedata(request.user),
            'auth': unicodedata(request.auth)  # "unicode" in the official DRF Guide
        }
        return Response(content)

    def post(self, request):
        content = request.POST.get()
        """
            if Angular login form data are valid():
                Retrieve Angular form fields and tell Angular to clean its form fields
                username = content of the Angular form username
                raw_password = content of the Angular form password
        """

        authenticated_user = authenticate(username=content.username, password=content.password)
        if authenticated_user and authenticated_user.is_active:
            django_login(request, authenticated_user)
            # return redirect('home_page')
            redirect_to = request.GET.get("next", "home_page")
            return redirect(redirect_to)
        else:
            pass
            # Tell Angular to notify the error "Usuario incorrecto o inactivo"
            # return render(request, "login_form.html", {'form': form})
        return Response(authenticated_user)


class RegisterView(APIView):

    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {
            'user': unicodedata(request.user),
            'auth': unicodedata(request.auth)
        }
        return Response(content)

    def post(self, request):
        # form = SignupForm(request.POST)
        """
        if Angular form data are valid():
            Retrieve Angular form fields and tell Angular to clean its form fields
            username = content of the Angular form username
            raw_password = content of the Angular form password
        """
        username = request.POST.get("username")   #   request.body.username  # form.get("username")
        raw_password = request.POST.get("password")
        print("The username is: " + username + "  " + raw_password)
        user = User.objects.create_user(username, raw_password)
        user.set_password(raw_password)
        user.save()
        authenticated_user = authenticate(username=username, password=raw_password)
        django_login(request, authenticated_user)
        # return Response(authenticated_user)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Tell Angular to redirect to the Home Page for that user


def logout(request):
    django_logout(request)
    # Tell Angular to redirect to the login page
