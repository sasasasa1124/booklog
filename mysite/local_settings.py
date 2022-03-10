import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'django-insecure-3ty(141te*lm%!7!%#*z(mo(uw#nlai7bytj8tyt8(4p7p^8l('

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'booklog',
        'USER': 'sasasasa1124',
        'PASSWORD': 'UTokyo3356!',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

DEBUG = True