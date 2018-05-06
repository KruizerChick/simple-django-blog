""" 
Django settings for the LOCAL / DEVELOPMENT environment 

- Run in Debug mode
- Use console backend for emails
- Add django-extensions as app
"""

from .base import *  # noqa


# GENERAL
# ------------------------------------------------------------------------------
# DEBUG = os.environ.get('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

ADMIN_URL = os.environ.get('DJANGO_ADMIN_URL', default='site-admin/')
ADMIN_DOCS_URL = os.environ.get('DJANGO_ADMIN_DOCS_URL', default='site-admin/doc/')

# ALLOWED_HOSTS = []

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = os.environ.get(
  'DJANGO_SECRET_KEY', default='#u-4r8+)0%&=@-e^g(==e7fld+i(482kb+3!ast07yqb9tv8m*')


# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'HOST': 'db',
#         'PORT': 5432,
#     }
# }


# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'


# THIRD-PARTY CONFIGURATIONS
# ------------------------------------------------------------------------------
# django-extensions
# INSTALLED_APPS += ['django_extensions', ]