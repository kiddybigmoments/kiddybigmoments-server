release: python manage.py migrate
web: gunicorn --log-file=- kiddybigmoments.wsgi:application
