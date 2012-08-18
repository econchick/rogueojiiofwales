# -*- coding: utf-8 -*-
import os

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

TEMPLATE_DEBUG = DEBUG = os.environ.get('DEBUG', False)

MANAGERS = ADMINS = ()

LANGUAGES = [('en', 'en')]
DEFAULT_LANGUAGE = 0
LANGUAGE_CODE = 'en'

SITE_ID = 1

assert 'SECRET_KEY' in os.environ, 'Set SECRET_KEY in your .env file!'
SECRET_KEY = os.environ['SECRET_KEY']

USE_L10N = USE_I18N = False

MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_DIR, 'compiled-static')
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'ghapi.middlewares.GithubAPIMiddleware',
]

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_login_redirect',
]

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = [
    os.path.join(PROJECT_DIR, 'templates'),
]

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'gunicorn',
    'south',
    'raven.contrib.django',
    'social_auth',
]

AUTHENTICATION_BACKENDS = [
    'social_auth.backends.contrib.github.GithubBackend',
    'django.contrib.auth.backends.ModelBackend',
]

LOGIN_URL          = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL    = '/login/failed/'


assert 'GITHUB_APP_ID' in os.environ, "Set GITHUB_APP_ID in your .env file!"
assert 'GITHUB_APP_SECRET' in os.environ, "Set GITHUB_APP_SECRET in your .env file!"
GITHUB_APP_ID = os.environ['GITHUB_APP_ID']
GITHUB_API_SECRET = os.environ['GITHUB_APP_SECRET']

try:
    from memcacheify import memcacheify
    CACHES = memcacheify()
except ImportError:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': 'not-so-unique-snowflake',
        }
    }

import dj_database_url

DATABASES = {'default': dj_database_url.config()}

RAVEN_CONFIG = {
    'dsn': os.environ.get("SENTRY_DSN", None),
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
