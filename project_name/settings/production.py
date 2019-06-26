# noinspection PyUnresolvedReferences
from .defaults import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'TODO',
        'USER': 'TODO',
        'PASSWORD': 'TODO',
        'HOST': 'TODO'
    }
}

DEBUG = False

ROOT_URLCONF = '%s.urls.production' % SITE_NAME

ALLOWED_HOSTS = ['TODO']
