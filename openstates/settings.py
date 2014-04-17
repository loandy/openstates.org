import os
from django.core.exceptions import ImproperlyConfigured

def envvar(name, default=None):
    result = os.environ.get(name, default)
    if result is None:
        raise ImproperlyConfigured('missing required environment variable ' + name)
    return result

# env variables
SECRET_KEY = envvar('SECRET_KEY')
RAVEN_DSN = envvar('RAVEN_DSN', '')
ALLOWED_HOSTS = envvar('ALLOWED_HOSTS', '*').split(',')
DATABASE_HOST = envvar('DATABASE_HOST', 'localhost')
DATABASE_NAME = envvar('DATABASE_NAME', 'api')
DATABASE_USER = envvar('DATABASE_USER', 'api')
DATABASE_ENGINE = envvar('DATABASE_ENGINE', 'django.db.backends.postgresql_psycopg2')
DATABASE_PASSWORD = envvar('DATABASE_PASSWORD', '')
IMAGO_MONGO_URI = envvar('IMAGO_MONGO_URI', 'mongodb://localhost')
TEMPATE_DEBUG = DEBUG = envvar('DJANGO_DEBUG', 'False').lower() == 'true'
USE_LOCKSMITH = envvar('USE_LOCKSMITH', 'False').lower() == 'true'
SUNLIGHT_AUTH_SECRET = envvar('SUNLIGHT_AUTH_SECRET', '')
if USE_LOCKSMITH:
    LOCKSMITH_SIGNING_KEY = envvar('LOCKSMITH_SIGNING_KEY')
    LOCKSMITH_MONGO_HOST = envvar('LOCKSMITH_MONGO_HOST', 'http://localhost:27017')
USE_S3_STORAGE = envvar('USE_S3_STORAGE', 'False').lower() == 'true'
if USE_S3_STORAGE:
    AWS_ACCESS_KEY_ID = envvar('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = envvar('AWS_SECRET_ACCESS_KEY')


DATABASES = {
    'default': {
        'NAME': DATABASE_NAME,
        'ENGINE': DATABASE_ENGINE,
        'HOST': DATABASE_HOST,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
    }
}

TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = False
USE_TZ = True

MEDIA_ROOT = ''
MEDIA_URL = ''

DATE_FORMAT = 'Y-m-d'
TIME_FORMAT = 'H:i:s'
DATETIME_FORMAT = 'Y-m-d H:i:s'

STATIC_ROOT = os.path.join(os.path.dirname(__file__), '..', 'collected_static')
STATIC_URL = '/media/'
STATICFILES_DIRS = (
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'media')),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

if USE_S3_STORAGE:
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    AWS_S3_SECURE_URLS = False
    AWS_LOCATION = 'assets/v3.1'
    AWS_S3_CUSTOM_DOMAIN = AWS_STORAGE_BUCKET_NAME = 'static.openstates.org'
    AWS_IS_GZIPPED = True
    AWS_HEADERS = {
            'Cache-Control': 'max-age=2592000',
            'Expires': 'Thu, 1 Jan 2015 12:34:56 GMT',
    }


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'openstates.urls'

WSGI_APPLICATION = 'openstates.wsgi.application'

TEMPLATE_DIRS = (
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates')),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.humanize',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'billy.web.api',
    'billy.web.admin',
    'billy.web.public',
    'social_auth',
    'markup_tags',
    'funfacts',
)

AUTHENTICATION_BACKENDS = (
    'sunlightauth.backends.SunlightBackend',
)

SUNLIGHT_AUTH_BASE_URL = 'https://login.sunlightfoundation.com/'
SUNLIGHT_AUTH_APP_ID = 'openstates'
SUNLIGHT_AUTH_SCOPE = []

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/sunlight/'

if USE_LOCKSMITH:
    LOCKSMITH_REGISTRATION_URL = 'http://services.sunlightlabs.com/accounts/register/'
    LOCKSMITH_HUB_URL = 'http://sunlightfoundation.com/api/analytics/'
    LOCKSMITH_API_NAME = 'openstates'
    LOCKSMITH_MONGO_DATABASE = 'openstates_locksmith'
    INSTALLED_APPS += ('locksmith.mongoauth',)
    MIDDLEWARE_CLASSES += ('locksmith.mongoauth.middleware.APIKeyMiddleware',)

if RAVEN_DSN:
    RAVEN_CONFIG = {
        'dsn': RAVEN_DSN
    }
    INSTALLED_APPS += ('raven.contrib.django.raven_compat',)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
