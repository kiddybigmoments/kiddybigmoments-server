from rest_framework import generics
from .models import Photo
from .serializers import PhotoSerializer


class ListPhotosView(generics.ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

