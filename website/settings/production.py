from __future__ import absolute_import, unicode_literals

from .base import *

SECRET_KEY = None
ALLOWED_HOSTS = None 

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'blog',
		'USER': 'blogger',
		'PASSWORD': None,
		'HOST': 'localhost',
		'PORT': '',
	}
}
