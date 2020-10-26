from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['proyecto-lider.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd2iddh5uq3sq6j',
        'USER': 'rmoydvzqkdcutr',
        'PASSWORD': '4b6cee16cec04e44181a882fce628434241bd63fe733eb5a719434d205d84208',
        'HOST':'ec2-54-156-53-71.compute-1.amazonaws.com',
        'DATABASE_PORT':'5432',
   }
}