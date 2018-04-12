# Back-end of Kiddybigmoments

### Development setup

1. Install Python 3.5+ and create the dependencies file: `pip freeze > requirements.txt` 
2. Install requirements using: `pip install -r requirements.txt`
3. Enter the folder where `manage.py` is located.
4. Create database and apply migrations: `python manage.py makemigrations` and `python manage.py migrate`
5. Run development server: `python manage.py runserver`


## Using the API

Each user has two fields: "number_of_kids" and an array of kids objects, like this:

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

All the endpoints require authentication, except the GET requests to **/api/1.0/users** and to **/api/1.0/posts**. 

## How to register a user

A **POST** request must be done.

http://localhost:8000/api/1.0/users

```
{
  "username": jose
  "email": jose@jose.com
}
 ```


## How to get a user token

The user must be registered in the application and do a **POST** request

http://localhost:8000/api/1.0/users/get-token

```
{
  "username": jose
  "password": supersegura
}
```

## Getting the users list

The user needs not to be registered and must do a **GET** request

http://localhost:8000/api/1.0/users

## Getting detailed information about the kids

Only a registered user can access and modify the information about his kids.

**GET** http://localhost:8000/api/1.0/kids

The fields retrieved are these ones:

```
{
    "title": "Título del artículo",
    "image": "http://images/my_image.com",
    "summary": "Resumen",
    "body": "Contenido",
    "publication_date": "2017-12-02",
    "category":[1, 2]
}
```

## Searching posts inside a blog

TODO

## Ordering a user's posts

The query parameter **order_by** is used.
Possible values are:
- **title**, **-title**
- **publication_date**, **-publication_date**

[Example: http://localhost:8000/api/1.0/posts/?order_by=title](http://localhost:8000/api/1.0/posts?order_by=title)  

## Creating a post

A **POST** request must be done to the url http://localhost:8000/api/1.0/posts/ with these two headers:

- **Content-Type**: set to application/json
- **Authorization**: set to token value

and these parameters in the body:

```
{
    "title": "Título del artículo",
    "image": "http://images/my_image.com",
    "summary": "Resumen",
    "body": "Contenido",
    "publication_date": "2017-12-02",
    "category":[1, 2]
}
```

## How to retrieve a post detail

Non-authenticated users can see only published posts.
Only the superuser and the author of that post can see a non-published post.

**GET**  [http://localhost:8000/api/1.0/posts/\<id\>](http://localhost:8000/api/1.0/posts/\<id\>)

## How to update a post detail

Only the superuser and the author of that post can perform this operation.

**PUT**  [http://localhost:8000/api/1.0/posts/\<id\>](http://localhost:8000/api/1.0/posts/\<id\>)

## How to delete a post detail

Only the superuser and the author of that post can perform this operation.

**DELETE**  [http://localhost:8000/api/1.0/posts/\<id\>](http://localhost:8000/api/1.0/posts/\<id\>)
                                        

