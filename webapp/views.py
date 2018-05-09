from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from webapp.models import Photo, Kid
from webapp.serializers import KidSerializer, PhotoSerializer, UserSerializer


class ListKidsView(generics.ListCreateAPIView):
    queryset = Kid.objects.all()
    serializer_class = KidSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)


class KidsDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
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
    permission_classes = (permissions.AllowAny,)
    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request):
            photo_serializer = PhotoSerializer(data=request.data)
            if photo_serializer.is_valid():
                photo_serializer.save()
                return Response(photo_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(photo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # (owner=self.request.user)


class PhotosDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)
    parser_classes = (FileUploadParser,)

