from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):

    login_username = forms.CharField(label="Nombre de usuario")
    login_password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, label="Nombre")
    last_name = forms.CharField(max_length=30, required=False, label="Apellidos")
    username = forms.CharField(max_length=30, required=True,  label="Nombre de usuario", help_text='Obligatorio.')
    email = forms.EmailField(max_length=254, required=False,  label="Correo electrónico")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'username', 'email', 'password1', 'password2',)
