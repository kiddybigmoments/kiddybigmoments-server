# Back-end of Kiddybigmoments

### Development setup

1. Install Python 3.4 or later. Create a virtual environment in Python and activate it. This can be done using the command-line or using the pyCharm graphical assistant.
2. Install the dependencies: `pip install -r requirements.txt`
3. Enter the folder where `manage.py` is located.
4. Create database and apply migrations: `python manage.py makemigrations` and `python manage.py migrate`
5. Create an admin user: `python manage.py createsuperuser`
6. Start the development server: `python manage.py runserver`


## Using the API

Each user will have two fields: "number_of_kids" and an array of kids objects, like this:

```
{
  "number_of_kids": "2",
    "kids": [
    {
      "name": "Antonio",
      "dateOfBirth": "12-enero-2011",
      "sex": "boy",
      "photos": [
      {
        "title": "Mi primer cumpleaños",
        "date": "12 de enero de 2012"
      },
      {
        "title": "Mis primeros balbuceos",
        "date": "octubre de 2011"
      }
      ]
    },
    {
      "name": "Elena",
      "dateOfBirth": "03-abril-2015",
      "sex": "girl",
      "photos": [
      {
        "title": "Mi primer cumpleaños",
        "date": "03 de abril de 2015"
      },
      {
        "title": "Mis primeros balbuceos",
        "date": "octubre de 2015"
      }
      ]

    }
  ]
}
```
Not implemented yet.

All the endpoints require authentication, except the login request.

## Existing endpoints

### api-token-auth

### auth/login
Not functional yet.

### api/v1/photos
It works only for GET requests.
