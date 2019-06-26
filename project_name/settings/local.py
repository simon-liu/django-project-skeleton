# noinspection PyUnresolvedReferences
from .defaults import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': './%s-dev.sqlite3' % SITE_NAME,
    }
}

DEBUG = True

ROOT_URLCONF = '%s.urls.development' % SITE_NAME

ALLOWED_HOSTS = ['*']

REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] = [
    'common.authentication.FakeAuthentication',
]
