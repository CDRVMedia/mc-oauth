"""
Django settings for mcoauth project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import os
import sys

import dj_database_url
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS, \
    AUTHENTICATION_BACKENDS
from django.core.urlresolvers import reverse_lazy


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret
# !! Generate your own. You may want to use the code below:
# from string import printable; from random import SystemRandom
# print ''.join([SystemRandom().choice(printable[:-6]) for c in range(50)])
SECRET_KEY = 'ar+HGtP4(^_xw-tXPy:4}!3<qgOQLSSRItCDTv<2`r7y!sp$Vs'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False') == 'True'  # default: False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

if 'test' in sys.argv:
    TESTING = True
else:
    TESTING = False

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'gunicorn',

    'mcoauth.core',
    'mcoauth.accounts',
    'mcoauth.mcaccounts',
    'mcoauth.api',

    'provider',
    'provider.oauth2',

    'bootstrap3',
    'registration',
    'sorl.thumbnail',

    # The following apps must be last
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
    'mcoauth.core.context_processors.domain',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

ROOT_URLCONF = 'mcoauth.urls'

WSGI_APPLICATION = 'mcoauth.wsgi.application'


DATABASES = {'default': dj_database_url.config(
    default='postgres://postgres:postgres@localhost/mcoauth-local')
}

if TESTING:
    DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
    DATABASES['default']['NAME'] = os.path.join(BASE_DIR, 'db.sqlite3')
    DATABASES['default']['AUTOCOMMIT'] = True


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = os.environ.get('STATIC_URL', '/static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

THUMBNAIL_BACKEND = 'mcoauth.mcaccounts.backends.thumbnail.ThumbnailBackend'

# AWS S3
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

USE_CLOUD_STORAGE = bool(AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY)

if USE_CLOUD_STORAGE:
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# Registration settings
AUTH_USER_MODEL = 'accounts.User'
ACCOUNT_ACTIVATION_DAYS = 7
LOGIN_REDIRECT_URL = reverse_lazy('dashboard')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_USER_AVATAR = 'images/default_user_avatar.png'

# OAuth settings
SCOPE_RETRIEVE_MINECRAFT_ACCOUNTS = 1 << 1

OAUTH_SCOPES = (
    (SCOPE_RETRIEVE_MINECRAFT_ACCOUNTS, 'retrieve_accounts'),
)

AUTHENTICATION_BACKENDS += (
    'mcoauth.mcaccounts.backends.authentication.MinecraftBackend',
)
