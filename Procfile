web: gunicorn backend.wsgi --log-file -
web: python manage.py migrate && gunicorn backend.wsgi
