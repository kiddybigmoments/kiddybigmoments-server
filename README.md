# Back-end of Kiddybigmoments

### Development setup

1. Install Python 3.4 or later. Create a virtual environment in Python and activate it. This can be done using the command-line or using the pyCharm graphical assistant.
2. Install the dependencies: `pip install -r requirements.txt`
3. Enter the folder where `manage.py` is located.
4. Create database and apply migrations: `python manage.py makemigrations` and `python manage.py migrate`
5. Create an admin user: `python manage.py createsuperuser`
6. Start the development server: `python manage.py runserver`


## Using the API

The Photo object has the following fields:

```
{
        "id": 1,
        "kids": [
            {
                "id": 1,
                "parents": {
                    "id": 1,
                    "mother": "pepita",
                    "father": "pepito"
                },
                "first_name": "Juanitoooo",
                "last_name": "López"
            }
        ],
        "title": "Foto 2",
        "description": "Esto es la foto del bautizo de Matías.",
        "image": "photos/baby.jpg",
        "created_at": "2018-04-18T21:09:03.793819Z",
        "modified_at": "2018-04-18T21:09:03.793873Z"
    }

```

The Parents object is the following:

```
{
        "id": 1,
        "mother": "pepita",
        "father": "pepito"
}
```

All the endpoints require authentication, except the login request.

## Existing endpoints

### api/v1/photos/

Only for GET requests.

### api/v1/photos/:id/

GET, BATCH, POST and DELETE requests for a certain photo.

### api/v1/parents/

Only for GET requests.

### api/v1/parents/:id/

GET, BATCH, POST and DELETE requests for a certain parent.

### api/v1/kids/

Only for GET requests.

### api/v1/kids/:id/

GET, BATCH, POST and DELETE requests for a certain kid.


### api/v1/register/

Fields: username, password.

**POST** request.

### api/v1/get-token/

Fields: username, password.

Returns two JWT tokens: called access and refresh. 

**POST** request.

### api/v1/refresh-token/

Refresh the token for registered user.

**POST** request.

More information on the library used for generating the JWT token can be found here: 
https://github.com/davesque/django-rest-framework-simplejwt#README.md
 

=============================================================

**NOTE**: login and logout are client endpoints, but not API endpoints.
