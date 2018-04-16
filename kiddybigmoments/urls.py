"""kiddybigmoments URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token

from webapp.views import ListPhotosView, LoginView, RegisterUsersView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth', obtain_jwt_token, name='create-token'),
    path('auth/register', RegisterUsersView.as_view(), name="auth-register"),
    path('auth/login', LoginView.as_view(), name="auth-login"),
    path('api/v1/photos', ListPhotosView.as_view(), name="photos-all"),


# API REST
    # path('api/1.0/hello', HelloWorld.as_view(), name="api_hello_world"),
    # path('api/1.0/photos', PhotosListAPI.as_view(), name="api_photos_list"),
    # path('api/1.0/photos/<int:pk>', PhotoDetailAPI.as_view(), name="api_photos_detail"),

]
