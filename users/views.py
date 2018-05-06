import unicodedata
from django.contrib import messages
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

from users.forms import SignupForm
from users.serializers import UsersListSerializer, UserSerializer
# from users.serializers import TokenSerializer


# class ListUsersView(APIView):
class ListUsersView(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        users = User.objects.all()   # users es un objeto que hay que convertir al formato de salida
        serializer = UsersListSerializer(users, many=True)
        # El serializador obtiene un diccionario por cada usuario de la lista
        return Response(serializer.data)

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


class LoginView(generics.CreateAPIView):

    # authentication_classes = (TokenAuthentication,)
    # serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()

    """
    def jwt_response_payload_handler(self, token, user=None, request=None):
        return {
            'token': token,
            'user': UserSerializer(user, context={'request': request}).data
        }
    """

    def post(self, request, *args, **kwargs):
        """
            if Angular login form data are valid():
                Retrieve Angular form fields and tell Angular to clean its form fields
                username = content of the Angular form username
                raw_password = content of the Angular form password
        """
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        authenticated_user = authenticate(request, username=username, password=password)
        if authenticated_user is not None:  # and authenticated_user.is_active:
            django_login(request, authenticated_user)
            serializer = TokenSerializer(data={
                # using drf jwt utility functions to generate a token
                "token": jwt_encode_handler(
                    jwt_payload_handler(authenticated_user)
                )})
            serializer.is_valid()
            django_login(request, authenticated_user)
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
            # return redirect('home_page')
            # redirect_to = request.GET.get("next", "home_page")
            # return redirect(redirect_to)
            # Tell Angular to notify the error "Usuario incorrecto o inactivo"
            # return render(request, "login_form.html", {'form': form})


class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()
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
        raw_password = request.data.get("password", "")
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
            # serializer.save()
            new_user = User.objects.create_user(
                username=username, password=raw_password
            )
            new_user.save()
            return Response(
                # data=serializer(new_user).data,
                data={
                    'username': username,
                    'password': raw_password
                },
                status=status.HTTP_201_CREATED
            )


"""
class LogoutView(generics.CreateAPIView):

    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        django_logout(request)
        return Response(status=status.HTTP_200_OK)
        # Tell Angular to redirect to the login page
"""