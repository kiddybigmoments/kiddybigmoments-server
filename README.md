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
                "first_name": "Matías",
                "last_name": "López"
            }
        ],
        "title": "Foto 2",
        "description": "Esto es la foto del bautizo de Matías.",
        "image_location": "https://www.piccolafesta.com/wp-content/uploads/2017/07/quq1-940x920-768x752.jpg",
        "created_at": "2018-04-18T21:09:03.793819Z",
        "modified_at": "2018-04-18T21:09:03.793873Z"
    },
```

All the endpoints require authentication, except the login request.

## Existing endpoints

### api-token-auth
Not functional yet.

### auth/login
Not functional yet.

### api/v1/photos

Only for GET requests.

### api/v1/photos/:id

GET, BATCH and DELETE requests for a certain photo.

### api/v1/kids

Only for GET requests.

### api/v1/kids/:id

GET, BATCH and DELETE requests for a certain kid.

## TBD
Endpoints for users. 
