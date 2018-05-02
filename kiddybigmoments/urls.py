"""kiddybigmoments URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
"""

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token

from kiddybigmoments import settings
from users.views import logout, RegisterView
from webapp.views import ListKidsView, ListPhotosView, KidsDetailView, PhotosDetailView, ListParentsView, \
    ParentsDetailView, UsersDetailView, ListUsersView
from webapp.views import LoginView, RegisterUsersView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/login/', LoginView.as_view(), name="api-login"),
    path('api/v1/logout/', logout, name="api-logout"),
    path('api/v1/register/', RegisterView.as_view(), name="api-register"),

    path('api/v1/users/', ListUsersView.as_view(), name="api-users-list"),
    path('api/v1/users/<int:pk>/', UsersDetailView.as_view(), name="api-users-detail"),
    # path('rest-auth/', include('rest_auth.urls'))

    path('api/v1/photos/', ListPhotosView.as_view(), name="api-photos-list"),
    path('api/v1/photos/<int:pk>/', PhotosDetailView.as_view(), name="api-photos-detail"),
    path('api/v1/kids/', ListKidsView.as_view(), name="api-kids-list"),
    path('api/v1/kids/<int:pk>/', KidsDetailView.as_view(), name="api-kids-detail"),
    path('api/v1/parents/', ListParentsView.as_view(), name="api-parents-list"),
    path('api/v1/parents/<int:pk>/', ParentsDetailView.as_view(), name="api-parents-detail"),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

