from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Photo
from .serializers import PhotoSerializer

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_photo(title=""):
        if title != "":
            Photo.objects.create(title=title)

    def setUp(self):
        self.create_photo("Foto 1")
        self.create_photo("Foto 2")
        self.create_photo("Foto 3")

    def test_get_all_photos(self):
        response = self.client.get(reverse("photos-all"))  # , kwargs={"v1"}))
        # fetch the data from db
        expected = Photo.objects.all()
        serialized = PhotoSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
