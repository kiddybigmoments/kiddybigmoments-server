from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from webapp.models import Photo, Kid
from webapp.serializers import KidSerializer, PhotoSerializer, UserSerializer


class ListKidsView(generics.ListCreateAPIView):
    serializer_class = KidSerializer
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return Kid.objects.all()


class KidsDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    queryset = Kid.objects.all()
    serializer_class = KidSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

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
    authentication_classes = (TokenAuthentication,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PhotosDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    authentication_classes = (TokenAuthentication,)
    parser_classes = (FileUploadParser,)

