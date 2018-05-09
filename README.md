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
                "name": "Juanito",
            }
        ],
        "title": "Foto 2",
        "description": "Esto es la foto del bautizo de Juan.",
        "image": "photos/baby.jpg",
        "created_at": "2018-04-18T21:09:03.793819Z",
        "modified_at": "2018-04-18T21:09:03.793873Z"
    }

```

## Existing endpoints

### api/v1/photos/

Only for GET requests.

### api/v1/photos/:id/

GET, BATCH, POST and DELETE requests for a certain photo.

### api/v1/kids/

Only for GET requests.

### api/v1/kids/:id/

GET, BATCH, POST and DELETE requests for a certain kid.


### rest-auth/registration/

Fields: username, password1, password2.

A session key is returned.

**POST** request.

### rest-auth/login/

Fields: username, password.

A session key is returned.

**POST** request.

### rest-auth/logout/

Fields: none.

**POST** request.

All the endpoints require authentication, except the login and the registration ones.

More information on the library used for login, logout and register can be found here: 
https://django-rest-auth.readthedocs.io/en/latest/api_endpoints.html
 

=============================================================

**NOTE**: a feature can be tested without using authentication, by changing the line 
`rest_framework.permissions.IsAuthenticated` to `rest_framework.permissions.AllowAny` in the file `settings.py`  
