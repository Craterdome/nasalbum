release: python manage.py migrate
web: gunicorn nasalbum.wsgi:application --env DJANGO_SETTINGS_MODULE='nasalbum.settings.heroku'
