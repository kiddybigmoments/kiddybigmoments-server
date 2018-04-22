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

from webapp.views import ListKidsView, ListPhotosView, KidsDetailView, PhotosDetailView, ListParentsView, ParentsDetailView
from webapp.views import LoginView, RegisterUsersView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth', obtain_jwt_token, name='create-token'),
    path('auth/register', RegisterUsersView.as_view(), name="auth-register"),
    path('auth/login', LoginView.as_view(), name="auth-login"),
    path('api/v1/photos', ListPhotosView.as_view(), name="api-photos-list"),
    path('api/v1/photos/<int:pk>', PhotosDetailView.as_view(), name="api-photos-detail"),
    path('api/v1/kids', ListKidsView.as_view(), name="api-kids-list"),
    path('api/v1/kids/<int:pk>', KidsDetailView.as_view(), name="api-kids-detail"),
    path('api/v1/users', ListParentsView.as_view(), name="api-users-list"),
    path('api/v1/users/<int:pk>', ParentsDetailView.as_view(), name="api-users-detail"),

]
