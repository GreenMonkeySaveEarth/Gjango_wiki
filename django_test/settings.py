# Django settings for django_test project.
import os
import dj_database_url


PROJECT_DIRECTORY = os.getcwd() 

DEBUG = False
#TEMPLATE_DEBUG = DEBUG
TEMPLATE_DEBUG = True

ADMINS = (
    ('Mike Hibbert', 'hibbert.michael@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': dj_database_url.config()
}



# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Greenwich'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/assets/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_DIRECTORY,'static/')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    ('assets', os.path.join(os.getcwd(),'static/')),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ads=q#_z%qwdok%wu(5j#8j_w(6nww9rs&amp;%t#gtrz69*_n2l+^'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'django_test.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'django_test.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIRECTORY,'templates/'),
    os.path.join(PROJECT_DIRECTORY,'articles/templates/'),
    os.path.join(PROJECT_DIRECTORY,'userprofile/templates/'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'whoosh',
    'haystack',
    'article',
    'south',
    'django.contrib.formtools',
    'userprofile',
    'storages',
    'approvals',
    'djcelery',
    'celery_test',
)

DELETE_MESSAGE = 50

MESSAGE_TAGS = {
    DELETE_MESSAGE : 'deleted',
}

TEMPLATE_CONTEXT_PROCESSORS = {
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',  
    'django.contrib.messages.context_processors.messages',
}


BROKER_HOST = "127.0.0.1"
BROKER_PORT = 5672
BROKER_VHOST = "/django_tutorials"
BROKER_USER = "mike"
BROKER_PASSWORD = "cheese"

import djcelery
djcelery.setup_loader()




LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
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

WHOOSH_INDEX = os.path.join(PROJECT_DIRECTORY,'whoosh/')


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': WHOOSH_INDEX,
    },
}

AUTH_PROFILE_MODULE = 'userprofile.UserProfile'

UPLOAD_FILE_PATTERN = "assets/uploaded_files/%s_%s"



FACEBOOK_APP_ID = ''
FACEBOOK_APP_SECRET = ''



AUTHENTICATION_BACKENDS = (
    'django_facebook.auth_backends.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)

try:
    from local_settings import *
except Exception as e:
    print e.message
    
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_PRELOAD_METADATA = True

if not DEBUG:    
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    S3_URL = 'http://%s.s3.amazonaws.com/assets/' % AWS_STORAGE_BUCKET_NAME
    STATIC_URL = S3_URL
    
    



