# noinspection PyUnresolvedReferences
from .defaults import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/ut-db.sqlite3',
    }
}

ETH_PROVIDER_URL = 'http://127.0.0.1:9545'
