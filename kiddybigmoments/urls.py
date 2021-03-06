"""kiddybigmoments URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
"""

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.conf.urls.static import static

from kiddybigmoments import settings
from users.views import ListUsersView, UsersDetailView
from webapp.views import ListKidsView, ListPhotosView, KidsDetailView, PhotosDetailView


urlpatterns = [
    path('admin/', admin.site.urls),


    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls'), name="api-registration"),
    # path('api/v1/rest-auth/authenticate-token/', ),    # TBD

    path('api/v1/users/', ListUsersView.as_view(), name="api-users-list"),
    path('api/v1/users/<int:pk>/', UsersDetailView.as_view(), name="api-users-detail"),

    path('api/v1/photos/', ListPhotosView.as_view(), name="api-photos-list"),
    path('api/v1/photos/<int:pk>/', PhotosDetailView.as_view(), name="api-photos-detail"),
    path('api/v1/kids/', ListKidsView.as_view(), name="api-kids-list"),
    path('api/v1/kids/<int:pk>/', KidsDetailView.as_view(), name="api-kids-detail"),

    path('files/', include('db_file_storage.urls')),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

