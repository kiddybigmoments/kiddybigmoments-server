from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.utils import json

from .models import Photo
from .serializers import PhotoSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_photo(title=""):
        if title != "":
            Photo.objects.create(title=title)

    def login_a_user(self, username="", password=""):
        url = reverse("auth-login")  # , kwargs={ "version": "v1" } )
        return self.client.post(
            url,
            data=json.dumps({
                "username": username,
                "password": password
            }),
            content_type="application/json"
        )

    def setUp(self):
        # create a admin user
        self.user = User.objects.create_superuser(
            username="test_user",
            email="test@mail.com",
            password="testing",
            first_name="test",
            last_name="user",
        )
        # add test data
        self.create_photo("Foto 1")
        self.create_photo("Foto 2")
        self.create_photo("Foto 3")

    def test_get_all_photos(self):
        self.login_client('test_user', 'testing')
        response = self.client.get(reverse("photos-all"))  # , kwargs={"v1"}))
        # fetch the data from db
        expected = Photo.objects.all()
        serialized = PhotoSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def login_client(self, username="", password=""):
        # get a token from DRF
        response = self.client.post(
            reverse('create-token'),
            data=json.dumps(
                {
                    'username': username,
                    'password': password
                }
            ),
            content_type='application/json'
        )
        self.token = response.data['token']
        # set the token in the header
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.token
        )
        self.client.login(username=username, password=password)
        return self.token


class AuthLoginUserTest(BaseViewTest):
    """
    Tests for the auth/login/ endpoint
    """

    def test_login_user_with_valid_credentials(self):
        # test login with valid credentials
        response = self.login_a_user("test_user", "testing")
        # assert token key exists
        self.assertIn("token", response.data)
        # assert status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # test login with invalid credentials
        response = self.login_a_user("anonymous", "pass")
        # assert status code is 401 UNAUTHORIZED
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class AuthRegisterUserTest(BaseViewTest):
    """
    Tests for auth/register/ endpoint
    """
    def test_register_a_user_with_valid_data(self):
        url = reverse("auth-register")
        response = self.client.post(
            url,
            data=json.dumps(
                {
                    "username": "new_user",
                    "password": "new_pass",
                    "email": "new_user@mail.com"
                }
            ),
            content_type="application/json"
        )
        # assert status code is 201 CREATED
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_a_user_with_invalid_data(self):
        url = reverse("auth-register")
        response = self.client.post(
            url,
            data=json.dumps(
                {
                    "username": "",
                    "password": "",
                    "email": ""
                }
            ),
            content_type='application/json'
        )
        # assert status code
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
