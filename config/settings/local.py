""" 
Django settings for the LOCAL / DEVELOPMENT environment 

- Run in Debug mode
- Use console backend for emails
- Add django-extensions as app
"""

from .base import *  # noqa


# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}


# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'


# THIRD-PARTY CONFIGURATIONS
# ------------------------------------------------------------------------------
# django-extensions
# INSTALLED_APPS += ['django_extensions', ]