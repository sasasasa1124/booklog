web: gunicorn mysite.wsgi --log-file -
release: python manage.py migrate && python manage.py loaddata data.json