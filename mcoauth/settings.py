"""
Django settings for mcoauth project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import os

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
from django.core.urlresolvers import reverse_lazy


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9y+h41#66jdn$*%%u!r4w*&*hjk2$8244*n(+1-7!ki8oz1_h8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'mcoauth.core',
    'mcoauth.accounts',
    'mcoauth.mcaccounts',

    'provider',
    'provider.oauth2',

    'bootstrap3',
    'registration',
    'sorl.thumbnail',
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


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

THUMBNAIL_BACKEND = 'mcoauth.mcaccounts.backends.thumbnail.ThumbnailBackend'

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
