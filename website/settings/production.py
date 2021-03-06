from __future__ import absolute_import, unicode_literals
from django.core.exceptions import ImproperlyConfigured
from .base import *


msg = "%s environment variable was not set."


def get_env_variable(env_var):
    try:
        return os.environ[env_var]
    except KeyError:
        error_msg = msg % env_var
        raise ImproperlyConfigured(error_msg)


try:
    from .local import *
except ImportError:
    pass

DEBUG = False

SECRET_KEY = get_env_variable("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = ['www.shawngustaw.com', 'shawngustaw.com', 'ec2-54-172-105-209.compute-1.amazonaws.com']

ADMINS = "errors@shawngustaw.com"

EMAIL_BACKEND = 'django_ses.SESBackend'

SERVER_EMAIL = "errors@shawngustaw.com"
DEFAULT_FROM_EMAIL = "me@shawngustaw.com"

# AWS Email backend config
AWS_ACCESS_KEY_ID = get_env_variable("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = get_env_variable("AWS_SECRET_ACCESS_KEY")
AWS_SES_REGION_NAME = 'us-east-1'
AWS_SES_REGION_ENDPOINT = 'email.us-east-1.amazonaws.com'

# Disqus
DISQUS_API_KEY = get_env_variable("DISQUS_API_KEY")
DISQUS_WEBSITE_SHORTNAME = get_env_variable("DISQUS_SHORT_NAME")

# Increased security for prod
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_HSTS_SECONDS = 3600
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = "DENY"

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'blog',
		'USER': 'blogger',
		'PASSWORD': get_env_variable("DJANGO_DB_PASS"),
		'HOST': 'localhost',
		'PORT': '',
	}
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '../log/error.log',
        },
        'file': {
            'level': 'CRITICAL',
            'class': 'logging.FileHandler',
            'filename': '../log/critical.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['file'],
            'level': 'CRITICAL',
            'propagate': True,
        },
    },
}
