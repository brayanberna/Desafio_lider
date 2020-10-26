from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['proyectovicky.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd7kun91l4tkktv',
        'USER': 'gnozderoccpbft',
        'PASSWORD': 'cf9df4ff7ba54bc5651cbcc055bb43156cd25d8201a1b870202722624ed7794c',
        'HOST':'ec2-3-210-255-177.compute-1.amazonaws.com',
        'DATABASE_PORT':'5432',
   }
}