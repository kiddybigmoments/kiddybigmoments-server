from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from webapp.models import Photo, Kid, Parents
from webapp.serializers import KidSerializer, PhotoSerializer, ParentsSerializer, UserSerializer


class ListKidsView(generics.ListCreateAPIView):
    serializer_class = KidSerializer

    def get_queryset(self):
        return Kid.objects.all()


class KidsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kid.objects.all()
    serializer_class = KidSerializer

    def get(self, request, *args, **kwargs):
        try:
            kid = self.queryset.get(pk=kwargs["pk"])
            return Response(KidSerializer(kid).data)
        except Kid.DoesNotExist:
            return Response(
                data={
                    "message": "Kid with id {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    # @validate_request_data
    # Source: https://github.com/kasulani/drf_tutorial/
    def put(self, request, *args, **kwargs):
        try:
            kid = self.queryset.get(pk=kwargs["pk"])
            serializer = KidSerializer()
            updated_kid = serializer.update(kid, request.data)
            return Response(KidSerializer(updated_kid).data)
        except Kid.DoesNotExist:
            return Response(
                data={
                    "message": "Kid with id {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


class ListPhotosView(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class PhotosDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    parser_classes = (FileUploadParser,)


class ListParentsView(generics.ListCreateAPIView):
    queryset = Parents.objects.all()
    serializer_class = ParentsSerializer

    #def perform_create(self, serializer):
    #    serializer.save(parents=self.request.user.username)


class ParentsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parents.objects.all()
    serializer_class = ParentsSerializer


